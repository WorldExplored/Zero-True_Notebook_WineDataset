import pandas as pd
from sklearn.datasets import load_wine
import zero_true as zt
import plotly.express as px

# Load the dataset and create DataFrame as before
wine = load_wine()
wine_df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
wine_df['wine_class'] = wine.target

# Correctly mapping target names
wine_df['wine_class'] = wine_df['wine_class'].apply(lambda x: wine.target_names[x])

# Define sliders
alcohol_slider = zt.RangeSlider(id='alcohol', min=wine_df.alcohol.min(), max=wine_df.alcohol.max(), step=0.1, label='Alcohol')
malic_acid_slider = zt.RangeSlider(id='malic_acid', min=wine_df.malic_acid.min(), max=wine_df.malic_acid.max(), step=0.01, label='Malic Acid')

# Assuming the 'zt.PlotlyComponent.from_figure' method exists and works as intended
# Define the callback function
def update_graph():
    # Filter the DataFrame based on slider values
    filtered_df = wine_df[(wine_df.alcohol >= alcohol_slider.value[0]) & (wine_df.alcohol <= alcohol_slider.value[1]) &
                          (wine_df.malic_acid >= malic_acid_slider.value[0]) & (wine_df.malic_acid <= malic_acid_slider.value[1])]
    
    # Create a new figure with filtered data
    fig = px.scatter(filtered_df, x='alcohol', y='malic_acid', color='wine_class',
                     hover_data=['proline'])

    fig.update_layout(
        title='Wine Dataset: Alcohol vs. Malic Acid',
        xaxis_title='Alcohol (%)',
        yaxis_title='Malic Acid'
    )
    
    # Update the PlotlyComponent with the new figure
    # This step assumes 'zt.PlotlyComponent.from_figure' can be used to update an existing component
    # If zt doesn't support direct updates, you may need to find an alternative method to refresh or redraw the component
    zt.PlotlyComponent.from_figure(id='wine_plt', figure=fig)

# Filter the DataFrame based on slider values
wline_df = wine_df[(wine_df.alcohol >= alcohol_slider.value[0]) & (wine_df.alcohol <= alcohol_slider.value[1]) &
                        (wine_df.malic_acid >= malic_acid_slider.value[0]) & (wine_df.malic_acid <= malic_acid_slider.value[1])]

fig = px.scatter(wline_df, x='alcohol', y='malic_acid', color='wine_class',
                     hover_data=['proline'])

fig.update_layout(
    title='Wine Dataset: Alcohol vs. Malic Acid',
    xaxis_title='Alcohol (%)',
    yaxis_title='Malic Acid'
)
zt.PlotlyComponent.from_figure(id='wine_plti', figure=fig)
