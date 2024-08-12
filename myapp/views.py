from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
import pandas as pd
from .email import send_summary_email

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            # Process the file using pandas
            df = pd.read_excel(file) if file.name.endswith('.xlsx') else pd.read_csv(file)
            # You can now handle the data in 'df' as needed
            
            # Group by 'Cust Pin' and count the occurrences
            summary_df = df.groupby('Cust Pin').agg({
            'Cust State': 'first',  # Take the first state associated with each Cust Pin
            'DPD': 'count'  # Count the number of occurrences for each Cust Pin
            }).reset_index()

            
            summary_df = summary_df[['Cust State', 'Cust Pin', 'DPD']]
            summary_df.columns = ['Cust State', 'Cust Pin', 'DPD(Count of Cust Pin)']
            print(summary_df)
            summary = summary_df.to_html(index=False)

            send_summary_email(summary)
            return render(request, 'summary.html', {'summary': summary})
    else:
        form = UploadFileForm()
    return render(request, 'home.html', {'form': form})
