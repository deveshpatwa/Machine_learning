# EDA

1. data load

2. dtypes check

3. type casting

4. duplicates dealing

5. outliers heandling (retain , rectify , remove)

6. zero varience , near zero varience features

7. handling null values

8. descretization - dummy variable, binarization, encoding(lable, one hot)

9. transformation - log, box-cox, yoejohnson - - check it with QQ plot

10. scaling - min-max, standardization, robust

# feature engineering

## 1. Scaling

Normlization in data - to reduce the range

Standardize   -1 to +1 

Min max scalar - always 0-1

**reburst scaler** - if data has outliers

> normalize the numeric data and convert category to numeric data

Encoding - converting category to numeric

1. binarization -
   
   1. dummy variables
   
   2. one hot encoding

2. pd.cut to make a categorical column
   
   # data transformation

## Feature engeneering

feature scaling

Learn QQ plot

learn probability plot - box cox plot

learn log transformation - np.log()

wisorization

jab tak scale nahi kiya tb tk log or boxoc nahi use ker skte - or ager nahi kiya to yeo- johnson transform



learn maths = matricx, determinents, eigine value, polynomials, linear algebra, calculas, differenceation, probability, partial differentiation , minima - maxima





# Auto EDA - nice if you want fast EDA

# find AI Tutor - website

# What is AI / ML

making machine capable of doing task which need a human intelligence to perform 

## type of AI - on how smart tey are

1. Narrow AI - choti soach ke jo sirf specific task ke liye bane hue he unable to independently to learn 

2. AGI - artificial general intelligence - general kam kerne ke liye noraml jo apn use kerte he

3. Artificial super intelligent

# types of ai based on functions

1. reachtive AI - jab tk koi action na do tb tk kam nahi karega
   
   2. limited memory - store memory of conversation
   
   3. Theory of Mind AI - can sense human emotions
   
   4. Self aware AI - Can understand human emotiona and self also
      
      ## Concept of AI
      
      1. ML and Deep Learning
      
      2. NLP - natural language
      
      3. CV - computer  vision
      
      4. Generative AI
      
      5. Explainable AI

# Types of machine learning

1. supervised 

2. Unsupervised

3. semi - supervised

4. reenforcement learning

> Q.how does ML programming differ from traditional programing?
> 
> IMP interview question

## supervised learning

1. regression analysis - numerical  - 
   
   1. general formula for regression -     y = mx + c for single and for multiple    y = m1x1(slop of variable 1 * value of x1) + m2x2(variable 2) + m3x3(variable one) + c (error) 
   
   2. how it is measured for how much error its throughing by 
      
      1. mean absolute error - same as mean absolute error MAD
      
      2. mean squred error - same as VAR
      
      3. root mean squre error - same as STD of error
      
      4. R squred is use to judge the result - between 1 and 0 where if near 1 its much better
   3. when its not predicting good you will use ridge , lasso, and elasticnet to improve its performance 
      1. l1 lasso regularization - shrink kerna he data - jab bahut sare columns ho (50+) or regression use kerna ho to lasso regression laga do 
      2. l2 ridge regularization - penalty ko add kerta he per sqr value kerke and near zero value deta he coeficient me - ye unscene data pe zyada acha kam kerta he 
      3. elastic net - 

2. classification - text / categorical
   to classify the data in categories
   types of classification - 
   how to check how good is your model
   
   1. accuracy - confusion matrix - [[tp,tn],[fp,fn]]   (percentage of how many times its correct / total prediction)
   2. precision score - tp / tp+fP
   3. recall  - tp / tp+fn
      **IVQ - difference between precision and recall**
      **IVQ - f1 score is harmonic mean of precision and recall**
   4. ROC / AUC curve - it will work on binary classification - its a trade of between tp and fp 

# Decission tree

tree like structure that is use to take decission using root, branch and leaf node

1. top down algorithm (greedy algoritm) - divide and conquer
2. mostely it work on categorical values
3. how decission tree deciside which category to choose from 
   - entropy - how pure and impure feature is
   - informatoin gain

# Ploynomial regression

   -- need to complete

# Logistic regression

   -- need to complete

# naive bayse

   -- need to complete

# KNN

works on both number and category, assume that the data near if similar

1. controlling complexity in K-NN - if k increase way more the it will become over fit
   > difference between over fitting and under fitting
   > whats biase and variance
   >what is  bias - variance trade off curve - it represent a struggle to build a modelthat finds the perfect balancebetween under fitting (high bias) and over fitting (high varience)
2. (assume closest distance from the historical datapoints and make predictions on them)
> whats lazy lerner and fast lerner

# Ensemble methods
   - combine more then one model to predict
   - hard voting just count the number of vote
   - soft voting use probability to predict voting 
   - weighted average bhi lete he isme

# Boosting ensemble learning
   1. Adaboost
      assign each 
   2. xgboost
   3. gradient boost


# Unsupervised learning
   model which dont need lables to learn 
   1. clustring
      - intra-class similarity 
      - inter-class similarity 
      - cluster of homogineus records 
      - create a scatter plot using only one column keep it in x and y also
      - agglomarative clustring(bottom up) and top down 
      - other algo , birch , etc
      - learn eculean distance using km and car drive example in a map
      - how to predict accuracy of model by silhouette score 
         (
            its range frome -1 to 1 where near to 1 mean good model(cluster are apart from each other) 
         and near to -1 means bad model(cluster are overlapping)
         )
   2. dimensionality reductions
      - LDA - linear discriminatoin
      - NMF - 
      - PCA  - imp try must
      - SVD  - imp must try
      - FA
      SOME NON LINEAR 
      - stocastic neighbor SNE
      - T-distribution stocastic neighbor embedding t-SEN
   3. K-means
   4. dbscan
    - market basket analysis
    - association rules application
      - **support** - number of combinantion / total transactions , this is use to consider only those transaction which are in higher frequency
      - **drawbacks** of these rules are , making all combinantion is exponencial , solve using iterative methods and level wise search
      - **Support**: How often an item group shows up in all records.Confidence: How often the second item appears when the first item is present.Lift: How much stronger a rule is than random chance.Algorithms: Common methods to find these rules include Apriori and FP-Growth.
      - The **lift ratio** measures how much more likely two items are to be bought together compared to if they were completely independent.
      - The benchmark in association rule mining refers to the expected baseline probability that the consequent (Y) will occur purely by random chance.
      - Leverage measures the difference between the actual co-occurrence of two items and the expected frequency if they were completely independent.While Lift is a ratio (multiplicative), Leverage is a difference (additive). It tells you how many additional transactions include both items because of their relationship.

     - antecedent is if and then is 
    - associatiotion rules faceplate - make combination for all most repeating combinantion, how to slect best one and usefull ones, 



# Hypothesis testing
   - sample t test , it use mean
   - mann whitney test , it use median
   - moods median test
   - paired t test
   - one way anova test , normality -> varience -> ANOVA(analysis of varience), here sum of sqr total = sum of sqr treatment + sum sqr of error 
   - H0 = null hypothesis
   - H1 = alternate hypothesis
   - if there are one factor / variable which is changing then we need one way anova test
   - but if there are two factore or varicable which are changing then we need two way anova test
   - Chi - square test - when we have more the 2 factore / variables whic are changing 


# stream lip deployment
   - streamlit run file_name.py (the file which has code of stream lip, you have to make a code using chatgpt givw him prompt to make this current file.py into a strealit )
   - after it is working on local host
   - then go to github and make a repository with that project name
   - you can add the descreption on it (optional)
   -  then go to streamlit cloud
   - connect github to streamlit website
   - create a app using github repo
   - select all option and make
   - 