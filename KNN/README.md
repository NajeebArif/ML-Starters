# k-nearest Neighbour

<p>
<i><b>It works like this:</b> we have an existing set of example data, our training set. We have
labels for all of this data—we know what class each piece of the data should fall into.
When we’re given a new piece of data without a label, we compare that new piece of
data to the existing data, every piece of existing data. We then take the most similar
pieces of data (the nearest neighbors) and look at their labels. We look at the top k
most similar pieces of data from our known dataset; this is where the k comes from. (k
is an integer and it’s usually less than 20.) Lastly, we take a majority vote from the k
most similar pieces of data, and the majority is the new class we assign to the data we
were asked to classify.</i>
</p>

<p>For a given data set and input value inX,<br/>
For every point in our dataset:<br/>
...calculate the distance between inX and the current point<br/>
...sort the distances in increasing order<br/>
...take k items with lowest distances to inX<br/>
...find the majority class among these items<br/>
...return the majority class as our prediction for the class of inX<br/>
</p><br/>

<p><ul>
<li><b>PROS</b>: High Accuracy, insensitive to outliers, no assumptions about data.</li>
<li><b>CONS</b>: Computationally expensive, requires a lot of memory</li>
<li><b>WORKS WITH</b>: Numeric values, nominal values</li>
</ul></p>