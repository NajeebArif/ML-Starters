# k-nearest Neighbour

<p>For a given data set and input value inX,<br/>
For every point in our dataset:<br/>
...calculate the distance between inX and the current point<br/>
...sort the distances in increasing order<br/>
...take k items with lowest distances to inX<br/>
...find the majority class among these items<br/>
...return the majority class as our prediction for the class of inX<br/>
</p><br/>

<b>PROS</b>: High Accuracy, insensitive to outliers, no assumptions about data.
<b>CONS</b>: Computationally expensive, requires a lot of memory
<b>WORKS WITH</b>: Numeric values, nominal values