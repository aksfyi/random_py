# OMDB Wrapper

Simple OMDB API wrapper (python). http://www.omdbapi.com/

## Usage

    from omdb import OMDB
    movdb = OMDB(api_key = "YOUR_API_KEY")

## Methods

 - **Search by IMDB ID / Title**
	 `search_by_imdb_or_title(self, imdb_id=None, title=None, vtype=None,
year_of_release=None, plot="short", version=1)`


 - **Search Movies**

        search(self, s=None, vtype=None,year_of_release=None, version=1, page=1):

 - Check http://www.omdbapi.com/ for the description about parameters

