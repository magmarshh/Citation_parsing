# Citation_parsing
Citation_parsing is a python tool that computes the number of times each citation is used in a given R Markdown File, useful in cutting down the number of citations in a manuscript to meet a journal's requirements. 


## Requirements
- python 3.7 
- re module 
- pandas module 
- csv module



## Usage
```{bash echo=FALSE}
citation_parsing.py -r <rmdfile> -o <outputfile> -i <ignore>
```

### Parameters

#### Required Parameters

- -r <rmdfile> : R Markdown file that will be parsed for citations
- -o <outputfile> : Desired name of output csv file with extension ".csv"

#### Optional Parameters
- -i <ignore> : list of any strings the user would like the program to ignore, possible example could be email addresses. Must be in the format of "ignore_word ignore_word", with the ignore words as one string surrounded by quotations and each ignore word separated by spaces. 



## Example

```{bash echo=FALSE}
python3.7 citation_parsing.py -r './test_data/test.Rmd' -o 'test.csv' -i 'stilianoudasc@mymail.vcu.edu marshallma4@mymail.vcu.edu mikhail.dozmorov@vcuhealth.org'
```



