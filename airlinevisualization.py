from google.colab import drive
drive.mount('/content/gdrive')

Go to this URL in a browser: https://accounts.google.com/o/oauth2/auth?client_id=947318989803-6bn6qk8qdgf4n4g3pfee6491hc0brc4i.apps.googleusercontent.com&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&scope=email%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdocs.test%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive.photos.readonly%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fpeopleapi.readonly&response_type=code

Enter your authorization code:
··········
Mounted at /content/gdrive

!ls "gdrive/My Drive/modifiedairlinefile.csv"

'gdrive/My Drive/modifiedairlinefile.csv'

import csv
import pandas as pd
import seaborn as sns

data = pd.read_csv("/content/gdrive/My Drive/modifiedairlinefile.csv")
g=sns.catplot(x="NumberOfAirlines", y="Country",
            kind="bar", data=data);
g.fig.set_figwidth(30)
g.fig.set_figheight(30)
