# Citation_parsing
Python tool that parses a Rmd File to count the number of times each citation is used. 









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



