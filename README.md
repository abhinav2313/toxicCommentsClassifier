# toxicCommentsClassifier
Cleaning up the internet one comment at a time using Neural Nets.   
Exploring methods of tokenizing input comments and constructing neural nets to determine level and type of toxicity of comments in an attempt to make the comment sections of the internet a better place.   

## What we need to do   
* Preprocess the text of the sample data in the most effective manner for analysis.   
   * tokenized versions for general analysis.   
   * n-grams for more effective analysis of relative meaning.   
      * ..."is a Nazi" vs "is not a Nazi" should register differently from each other
   * whatever manner best suits the various net setups.   
      * TBD

* build Recursive Neural Nets.   
  * analyses lexical structures together with previous structures.
* build Recurrent Neural Nets?
  * analyses each word/n-gram/whatever unit with respect to the previous units
* build Vanilla Neural Nets
  * for initial analysis at least
