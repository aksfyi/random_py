"""
author : Akshay T
OMDB API wrapper
"""


import requests
from .omdberrors import OMDBParamError, OMDBResponseError, APIRequestError


class OMDB:
    """
    OMDB class
    Parameters for creating object: api_key

    """
    types = ["movie", "series", "episode"]
    plots = ["short", "full"]
    base_url = "http://omdbapi.com/"

    def __init__(self, api_key=None):
        self.api_key = api_key
        self.params = dict()

    def __checkresponse(self, resp):
        """
            Function to check if the api response is valid
        """
        if resp['Response'] == "False":
            raise OMDBResponseError(resp["Error"])
        else:
            return resp

    def __checktype(self, vtype):
        """
            Function to check if the entered type
            is valid
        """
        if vtype not in OMDB.types:
            raise OMDBParamError("Invalid Parameter : Type")

    def __checkplot(self, plot):
        """
            Function to check if the entered type
            is valid
        """
        if plot not in OMDB.plots:
            raise OMDBParamError("Invalid Parameter : Plot")

    def __set_params(self, vtype, year, plot, version):
        self.params["v"] = version
        self.params["apikey"] = self.api_key
        if vtype is not None:
            try:
                self.__checktype(vtype.lower().strip())
                self.params["type"] = vtype
            except Exception as e:
                err = f"Invalid Parameter : vtype :: {str(e)}"
                raise OMDBParamError(err)
        if plot is not None:
            try:
                self.__checkplot(plot.lower().strip())
                self.params["plot"] = plot
            except Exception as e:
                err = f"Invalid Parameter : plot :: {str(e)}"
                raise OMDBParamError(err)

        if year is not None:
            self.params["y"] = year

    def __send_response(self):
        try:
            r = requests.get(OMDB.base_url, params=self.params)
            return self.__checkresponse(r.json())
        except Exception as e:
            err = f"Failed to send API Request : {str(e)}"
            raise APIRequestError(err)

    def search_by_imdb_or_title(self, imdb_id=None, title=None, vtype=None,
                                year_of_release=None, plot="short", version=1):
        """
            function to list movie details by imdb_id or title

        """
        if "page" in self.params:
            del self.params["page"]
        if "s" in self.params:
            del self.params["s"]

        self.__set_params(vtype=vtype, year=year_of_release,
                          plot=plot, version=version)

        if imdb_id is not None:
            self.params["i"] = imdb_id
        elif title is not None:
            self.params["t"] = title
        return self.__send_response()

    def search(self, s=None, vtype=None,
               year_of_release=None, version=1, page=1):
        """
        get list of movies/series 
        s: search term
        """
        if s is None:
            err = "search term is None"
            raise OMDBParamError(err)

        if "i" in self.params:
            del self.params["i"]
        if "t" in self.params:
            del self.params["t"]
        self.params["page"] = page
        self.params["s"] = s.strip()
        self.__set_params(vtype=vtype, plot=None,
                          year=year_of_release, version=version)

        return self.__send_response()
