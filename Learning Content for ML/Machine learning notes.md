Zero variance 

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

### supervised learning

1. regression analysis - numerical  - 
   
   1. general formula for regression -     y = mx + c for single and for multiple    y = m1x1(slop of variable 1 * value of x1) + m2x2(variable 2) + m3x3(variable one) + c (error) 
   
   2. how it is measured for how much error its throughing by 
      
      1. mean absolute error - same as mean absolute error MAD
      
      2. mean squred error - same as VAR
      
      3. root mean squre error - same as STD of error
      
      4. R squred is use to judge the result - between 1 and 0 where if near 1 its much better

2. classification - text / categorical
   to classify the data in categories
   types of classification - 
   how to check how good is your model
   
   1. accuracy - confusion matrix - [[tp,tn],[fp,fn]]   (percentage of how many times its correct / total prediction)
   2. precision score - tp / tp+fP
   3. recall  - tp / tp+fn
      **IVQ - difference between precision and recall**
      **IVQ - f1 score is harmonic mean of precision and recall**
      ![confusion matrix](file:///C:/Users/deves/Documents/GitHub/Machine_learning/Learning%20Content%20for%20ML/confusion-matrix.webp)
   4. ROC / AUC curve - it will work on binary classification - its a trade of between tp and fp 

# Decission tree
tree like structure that is use to take decission using root, branch and leaf node
   1. top down algorithm (greedy algoritm) - divide and conquer
   2. mostely it work on categorical values
   3. how decission tree deciside which category to choose from 
      - entropy - how pure and impure feature is
      - informatoin gain