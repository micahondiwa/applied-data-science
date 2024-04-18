import math

import numpy as np
import plotly.express as px
import scipy
from database import MongoRepository

from statsmodels.stats.contingency_tables import Table2x2
from statsmodels.stats.power import GofChisquarePower
#from teaching_tools.ab_test.experiment import Experiment


# Tasks 7.4.7, 7.4.9, 7.4.10, 7.4.19
class GraphBuilder:
    """Methods for building Graphs."""

    def __init__(self, repo=MongoRepository()):

        """init

        Parameters
        ----------
        repo : MongoRepository, optional
            Data source, by default MongoRepository()
        """
        pass

    def build_nat_choropleth():

        """Creates nationality choropleth map.

        Returns
        -------
        Figure
        """
        # Get nationality counts from database
        
        # Create Figure
        
        # Return Figure
        pass

    def build_age_hist():

        """Create age histogram.

        Returns
        -------
        Figure
        """
        # Get ages from respository

        # Create Figure
        
        # Return Figure
        pass

    def build_ed_bar():

        """Creates education level bar chart.

        Returns
        -------
        Figure
        """
        # Get education level value counts from repo

        # Create Figure
        
        # Return Figure
        pass

    def build_contingency_bar():

        """Creates side-by-side bar chart from contingency table.

        Returns
        -------
        Figure
        """
        # Get contingency table data from repo

        # Create Figure
        
        # Return Figure
        pass


# Tasks 7.4.12, 7.4.18, 7.4.20
class StatsBuilder:
    """Methods for statistical analysis."""

    def __init__():

        """init

        Parameters
        ----------
        repo : MongoRepository, optional
            Data source, by default MongoRepository()
        """
        pass

    def calculate_n_obs():

        """Calculate the number of observations needed to detect effect size.

        Parameters
        ----------
        effect_size : float
            Effect size you want to be able to detect

        Returns
        -------
        int
            Total number of observations needed, across two experimental groups.
        """
        # Calculate group size, w/ alpha=0.05 and power=0.8
        
        # Return number of observations (group size * 2)
        pass

    def calculate_cdf_pct():

        """Calculate percent chance of gathering specified number of observations in
        specified number of days.

        Parameters
        ----------
        n_obs : int
            Number of observations you want to gather.
        days : int
            Number of days you will run experiment.

        Returns
        -------
        float
            Percentage chance of gathering ``n_obs`` or more in ``days``.
        """
        # Calculate quiz per day mean and std
        
        # Calculate mean and std for days
        
        # Calculate CDF probability, subtract from 1
        
        # Turn probability to percentage

        # Return percentage
        pass

    def run_experiment():

        """Run experiment. Add results to repository.

        Parameters
        ----------
        days : int
            Number of days to run experiment for.
        """
        # Instantiate Experiment
        
        # Reset experiment

        # Run experiment for days
        pass

    def run_chi_square():

        """Tests nominal association.

        Returns
        -------
        A bunch containing the following attributes:

        statistic: float
            The chi^2 test statistic.

        df: int
            The degrees of freedom of the reference distribution

        pvalue: float
            The p-value for the test.
        """
        # Get data from repo

        # Create `Table2X2` from data

        # Run chi-square test

        # Return chi-square results
        pass
