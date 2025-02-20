URL: https://docs.cohere.com/reference/embed
---
🚀 Announcement: New API V2 endpoints are available! ( [Learn more](https://cohere.com/blog/new-api-v2)) 🚀

This endpoint returns text embeddings. An embedding is a list of floating point numbers that captures semantic information about the text that it represents.

Embeddings can be used to create text classifiers as well as empower semantic search. To learn more about embeddings, see the embedding page.

If you want to learn more how to use the embedding model, have a look at the [Semantic Search Guide](https://docs.cohere.com/docs/semantic-search).

### Headers

X-Client-NamestringOptional

The name of the project that is making the request.

### Request

This endpoint expects an object.

modelstringRequired

Defaults to embed-english-v2.0

The identifier of the model. Smaller “light” models are faster, while larger models will perform better. [Custom models](https://docs.cohere.com/docs/training-custom-models) can also be supplied with their full ID.

Available models and corresponding embedding dimensions:

- `embed-english-v3.0` 1024

- `embed-multilingual-v3.0` 1024

- `embed-english-light-v3.0` 384

- `embed-multilingual-light-v3.0` 384

- `embed-english-v2.0` 4096

- `embed-english-light-v2.0` 1024

- `embed-multilingual-v2.0` 768


input\_typeenumRequired

Allowed values: search\_documentsearch\_queryclassificationclusteringimage

Specifies the type of input passed to the model. Required for embedding models v3 and higher.

- `"search_document"`: Used for embeddings stored in a vector database for search use-cases.
- `"search_query"`: Used for embeddings of search queries run against a vector DB to find relevant documents.
- `"classification"`: Used for embeddings passed through a text classifier.
- `"clustering"`: Used for the embeddings run through a clustering algorithm.
- `"image"`: Used for embeddings with image input.

embedding\_typeslist of enumsRequired

Allowed values: floatint8uint8binaryubinary

Specifies the types of embeddings you want to get back. Can be one or more of the following types.

- `"float"`: Use this when you want to get back the default float embeddings. Valid for all models.
- `"int8"`: Use this when you want to get back signed int8 embeddings. Valid for only v3 models.
- `"uint8"`: Use this when you want to get back unsigned int8 embeddings. Valid for only v3 models.
- `"binary"`: Use this when you want to get back signed binary embeddings. Valid for only v3 models.
- `"ubinary"`: Use this when you want to get back unsigned binary embeddings. Valid for only v3 models.

textslist of stringsOptional

An array of strings for the model to embed. Maximum number of texts per call is `96`. We recommend reducing the length of each text to be under `512` tokens for optimal quality.

imageslist of stringsOptional

An array of image data URIs for the model to embed. Maximum number of images per call is `1`.

The image must be a valid [data URI](https://developer.mozilla.org/en-US/docs/Web/URI/Schemes/data). The image must be in either `image/jpeg` or `image/png` format and has a maximum size of 5MB.

truncateenumOptionalDefaults to `END`

Allowed values: NONESTARTEND

One of `NONE|START|END` to specify how the API will handle inputs longer than the maximum token length.

Passing `START` will discard the start of the input. `END` will discard the end of the input. In both cases, input is discarded until the remaining input is exactly the maximum input token length for the model.

If `NONE` is selected, when the input exceeds the maximum input token length an error will be returned.

### Response

This endpoint returns an object.

idstring

embeddingsobject

An object with different embedding types. The length of each embedding type array will be the same as the length of the original `texts` array.

Show 5 properties

textslist of strings

The text entries for which embeddings were returned.

imageslist of objectsOptional

The image entries for which embeddings were returned.

Show 4 properties

metaobjectOptional

Show 4 properties

[Create an Embed Job\\
\\
Up Next](/reference/create-embed-job)

[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=docs.cohere.com)