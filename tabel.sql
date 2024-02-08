SELECT * FROM wine_df
WHERE (alcohol BETWEEN {alcohol_slider.value[0]} AND {alcohol_slider.value[1]})
AND (malic_acid BETWEEN {malic_acid_slider.value[0]} AND {malic_acid_slider.value[1]}