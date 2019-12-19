# Create a pandas dataframe with demo data:
import pandas as pd
demodata_csv = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
df = pd.read_csv(demodata_csv)

# Pretty print the dataframe as an html table to a file
intermediate_html = '/tmp/intermediate.html'
#to_html_pretty(df,intermediate_html,'Iris Data')
# if you do not want pretty printing, just use pandas:
# df.to_html(intermediate_html)

# Convert the html file to a pdf file using weasyprint
import weasyprint
out_pdf= '/tmp/demo.pdf'
weasyprint.HTML(intermediate_html).write_pdf(out_pdf)