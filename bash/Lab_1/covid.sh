#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
NEWPOSITIVE=$(echo $DATA | jq '.[0].positiveIncrease')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalizedCurrently')
ONVENTILATOR=$(echo $DATA | jq '.[0].onVentilatorCurrently')
HOSPICEINCREASE=$(echo $DATA | jq '.[0].hospitalizedIncrease')

TODAY=$(date)

echo "On $TODAY, there were $NEWPOSITIVE new positive COVID cases, a $HOSPICEINCREASE increase in hospitalizations, with $HOSPITALIZED people currently hospitalized, and $ONVENTILATOR people on ventilators in the U.S."
