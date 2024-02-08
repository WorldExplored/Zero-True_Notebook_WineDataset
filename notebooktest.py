import pandas as pd
from sklearn.datasets import load_wine
import zero_true as zt

# Load the wine dataset
wine = load_wine()

# Create a DataFrame from the wine dataset
wine_df = pd.DataFrame(data=wine.data, columns=wine.feature_names)

# Add a column for the wine labels
wine_df['wine_class'] = [wine.target_names[i] for i in wine.target]

# Since the wine dataset column names don't have spaces or units like 'cm', we might not need to rename them for simplicity.
# However, if you still want to ensure consistency or format them, you could do so similarly:
wine_df.columns = [col.replace(' ', '_') for col in wine_df.columns]

# You would then adjust the sliders to match the wine dataset's features.
# Here's an example for alcohol and malic_acid, assuming zero_true's RangeSlider works similarly for any dataset:
alcohol_slider = zt.RangeSlider(id='alcohol',
                                min=wine_df.alcohol.min(),
                                max=wine_df.alcohol.max(),
                                step=0.1, label='Alcohol')

malic_acid_slider = zt.RangeSlider(id='malic_acid',
                                   min=wine_df.malic_acid.min(),
                                   max=wine_df.malic_acid.max(),
                                   step=0.01, label='Malic Acid')

# Example sliders for other features can be created in a similar fashion.


import plotly.express as px
import zero_true as zt

# Assuming wine_df is your DataFrame name and it's already loaded with the wine dataset
fig = px.scatter(wine_df, x='alcohol', y='malic_acid', color='color_intensity',
                 size='hue', hover_data=['proline'])

fig.update_layout(
    title='Wine Dataset: Alcohol vs. Malic Acid',
    xaxis_title='Alcohol (%)',
    yaxis_title='Malic Acid'
)

zt.PlotlyComponent.from_figure(id='wine_plt', figure=fig)
