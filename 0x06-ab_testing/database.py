import pandas as pd
from country_converter import CountryConverter
from pymongo import MongoClient


# Tasks 7.4.5, 7.4.6, 7.4.9, 7.4.10
class MongoRepository:
    """For connecting and interacting with MongoDB."""

    def __init__(
        self,
        client=MongoClient(host="localhost", port=27017),
        db="wqu-abtest",
        collection="ds-applicants"
    ):
    
        """init

        Parameters
        ----------
        client : pymongo.MongoClient, optional
            By default MongoClient(host="localhost", port=27017)
        db : str, optional
            By default "wqu-abtest"
        collection : str, optional
            By default "ds-applicants"
        """
        self.collection=client[db][collection]
        

    def get_nationality_value_counts(self, normalize=True):
    
        """Return nationality value counts.

        Parameters
        ----------
        normalize : bool, optional
            Whether to normalize frequency counts, by default True

        Returns
        -------
        pd.DataFrame
            Database results with columns: 'count', 'country_name', 'country_iso2',
            'country_iso3'.
        """
        # Get result from database
        result = ds_app.aggregate(
            [
                {
                    "$group": {
                        "_id": "$countryISO2","count": {"$count": {}}
                        }
                    }
                ]
        )
        # Store result in DataFrame
        df_nationality = pd.DataFrame(result).rename({"_id":"country_iso2"}, axis="columns").sort_values("count")
        
        # Add country names and ISO3
        cc = CountryConverter()
        df_nationality["country_name"] = cc.convert(df_nationality["country_iso2"], to="name_short")
        
        # Transform frequency count to pct
        
        # Return DataFrame
        pass

    def get_ages():

        """Gets applicants ages from database.

        Returns
        -------
        pd.Series
        """
        # Get ages from database
        
        # Load results into series

        # Return ages
        pass

    def __ed_sort():

        """Helper function for self.get_ed_value_counts."""
        pass
        

    def get_ed_value_counts():

        """Gets value counts of applicant eduction levels.

        Parameters
        ----------
        normalize : bool, optional
            Whether or not to return normalized value counts, by default False

        Returns
        -------
        pd.Series
            W/ index sorted by education level
        """
        # Get degree value counts from database
        
        # Load result into Series
        
        # Sort Series using `self.__ed_sort`

        # Optional: Normalize Series
        
        # Return Series
        pass

    def get_no_quiz_per_day():

        """Calculates number of no-quiz applicants per day.

        Returns
        -------
        pd.Series
        """
        # Get daily counts from database
        
        # Load result into Series
        
        # Return Series
        pass

    def get_contingency_table():

        """After experiment is run, creates crosstab of experimental groups
        by quiz completion.

        Returns
        -------
        pd.DataFrame
            2x2 crosstab
        """
        # Get observations from database

        # Load result into DataFrame

        # Create cross-tab from DataFrame
        
        # Return cross-tab
        pass
