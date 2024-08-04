from django.shortcuts import render
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64

def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        if uploaded_file and uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
            
            # Handling missing values in 'Sleep Duration'
            if 'Sleep Duration' in df.columns:
                df['Sleep Duration'] = pd.to_numeric(df['Sleep Duration'], errors='coerce')
                df = df.dropna(subset=['Sleep Duration'])

                # To Extract the first 10 rows
                first_10_rows = df.head(10)
                first_10_rows_html = first_10_rows.to_html(classes='table table-striped', index=False)

                # To Analyze and plot the 'Sleep Duration' column
                column_to_analyze = 'Sleep Duration'
                
                try:
                    # Calculate statistics
                    mean_val = df[column_to_analyze].mean()
                    median_val = df[column_to_analyze].median()
                    std_dev_val = df[column_to_analyze].std()
                    
                    # Plotting the data
                    sns.histplot(df[column_to_analyze], kde=True)
                    plt.xlabel(column_to_analyze)
                    plt.ylabel('Frequency')
                    plt.title(f'Distribution of {column_to_analyze}')
                    
                    # Save the plot to a BytesIO object and convert to base64
                    buffer = io.BytesIO()
                    plt.savefig(buffer, format='png')
                    plt.close()
                    buffer.seek(0)
                    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
                    
                    # Passing statistics, plot, and data to the template
                    context = {
                        'image_base64': image_base64,
                        'mean': mean_val,
                        'median': median_val,
                        'std_dev': std_dev_val,
                        'first_10_rows_html': first_10_rows_html,
                    }
                    return render(request, 'data_analysis/result.html', context)
                except KeyError:
                    return render(request, 'data_analysis/result.html', {'error': 'Specified column does not exist in the dataset.'})
            else:
                return render(request, 'data_analysis/upload.html', {'error': 'The "Sleep Duration" column is missing or contains no valid data.'})
        else:
            return render(request, 'data_analysis/upload.html', {'error': 'Please upload a valid CSV file.'})
    
    return render(request, 'data_analysis/upload.html')