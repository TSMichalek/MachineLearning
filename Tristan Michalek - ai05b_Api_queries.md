# API Query Building Assignment
---

## USGS Earthquake Queries

### Query 1: [statistics of earthquakes with a minimum magnitude of 5]
**URL:**
```
https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minmagnitude=5.0&limit=10
```

**Parameters used:**
- `format`: [geojson]
- `parameter2`: [magnitude=5]
- `parameter3`: [limit=10]

**Result:** [10 earthquakes, magnitude range: 5.0-6.1]

---

### Query 2: [10 earthquakes, in the western boundary ordered by magnitude]
**URL:**
```
https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minlongitude=-130&orderby=magnitude
```

**Parameters used:**
- `format`: [geojson]
- `minlongitude`: [-130]
- `orderby`: [magnitude]

**Result:** [Sarangani, Philippines, with 6.4]

---

### Query 3: [10 earthquakes, in the Eastern boundary ordered by magnitude]
**URL:**
```
https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&maxlongitude=-60&orderby=magnitude
```

**Parameters used:**
- `format`: [geojson]
- `maxlongitude`: [-60]
- `orderby`: [magnitude]

**Result:** [Kermadec Islands, New Zealand, with 6.1]

---

## Open Library Queries

### Query 4: [10 books written by J. K. Rowling, specifically returning the title and publish year]
**URL:**
```
https://openlibrary.org/search.json?author=j+k+rowling&fields=title,first_publish_year&limit=10
```

**Parameters used:**
- `author`: [J. K. Rowling]
- `fields`: [title, first publishing year]
- `limit`: [10]

**Result:** [10 Harry Potter books, released from 1997-2012]


### Query 5: [10 books written by Tolkien, title and publishing year]
**URL:**
```
https://openlibrary.org/search.json?author=tolkien&fields=title,first_publish_year&limit=10
```

**Parameters used:**
- `author`: [Tolkien]
- `fields`: [title, first publishing year]
- `limit`: [10]

**Result:** [Books range from 1937 (The Hobbit) to 2001 (The Children of Húrin)]

### Query 6: [3 history books]
**URL:**
```
https://openlibrary.org/search.json?subject=history&limit=3&fields=title
```

**Parameters used:**
- `subject`: [history]
- `fields`: [title]
- `limit`: [3]

**Result:** [The Story of Philosophy, Записки изъ подполья, The Enduring Vision]