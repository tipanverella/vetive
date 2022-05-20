Sa a se yon model antite pou proje a:

```mermaid
erDiagram
    PUBLISHER ||--o{ VIDEO : posts
    CONTEXT ||--o{ VIDEO: is
    PUBLISHER {
        string ID
        string name
        string description
    }
    VIDEO {
        string ID
        string title
        string description
        string language
        string publihser_id
    }    
    CONTEXT {
        string video_id
        string publisher_id
    }
```
