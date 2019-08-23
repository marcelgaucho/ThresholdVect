# Threshold Vect

Processing plugin-based provider that adds a model to polygonize a raster from a lower and an upper threshold.

The model added is named TV Vectorization Threshold. For this model to work, the plugin adds this and other models to a group called ThresholdVect, and scripts to a group with the same name.

There are a number of parameters that can be set to optimize the polygonization. These parameters are described in the help of the model. It includes smallest area and smallest hole for the polygons, tolerance and method for the simplification, an optional extent to polygonize only part of the raster, the size of a buffer for aggregation of polygons by the simple approach buffer-dissolve-debuffer.

Also, a model is added to calculate the `NDWI`, a possible input to the plugin model that can be used to extract water bodies. To extract water bodies using NDWI, perform the following 2 steps:

1- Extract NDWI using the TV Raster NDWI or TV Multiband NDWI model, depending on whether the bands are in different rasters or in a single raster.
2- Execute the TV Vectorization Threshold model. 

The plugin code is based on the Append Features to Layer plugin.

# Threshold Vect

Provedor do Processing que inclui um modelo para vetorização de um raster a partir de um limiar inferior e um superior.

O modelo adicionado é denominado TV Vectorization Threshold. Para que esse modelo funcione, o plugin adiciona este e outros modelos a um grupo chamado ThresholdVect, e scripts a um grupo com o mesmo nome.

Há vários parâmetros que podem ser configurados para otimizar a vetorização. Esses parâmetros são descritos na ajuda do modelo. Eles incluem  menor área e menor buraco para os polígonos, tolerância e método para a simplificação, uma extensão opcional para poligonizar apenas parte do raster, o tamanho de um buffer para amalgamação de polígonos pela simples abordagem buffer-dissolver-debuffer.

Além disso, um modelo é adicionado para calcular o NDWI, uma possível entrada para o modelo do plugin que pode ser usada para extrair massas d'água. Para extrair corpos de água usando o NDWI, execute os 2 passos seguintes:

1- Extraia o NDWI usando o modelo TV Raster NDWI ou TV Multiband NDWI, dependendo se as bandas estão em diferentes rasters ou em um único raster.
2- Execute o modelo TV Vectorization Threshold.

O código do plugin é baseado no do plugin Append Features to Layer.
