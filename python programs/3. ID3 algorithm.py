class DecisionTreeClassifier:
    """Decision Tree Classifier using ID3 algorithm."""

    def __init__(self, X, feature_names, labels):
        self.X = X  # features or predictors
        self.feature_names = feature_names  # name of the features
        self.labels = labels  # categories
        self.labelCategories = list(set(labels))  # unique categories
        # number of instances of each category
        self.labelCategoriesCount = [list(labels).count(x) for x in self.labelCategories]
        self.node = None  # nodes
        # calculate the initial entropy of the system
        self.entropy = self._get_entropy([x for x in range(len(self.labels))])
        def _get_entropy(self, x_ids):

# sorted labels by instance id
labels = [self.labels[i] for i in x_ids]:
# count number of instances of each category
label_count = [labels.count(x) for x in self.labelCategories]
# calculate the entropy for each category and sum them
entropy = sum([-count / len(x_ids) * math.log(count / len(x_ids), 2)
                   if count else 0
                   for count in label_count
                  ])
        
        return entropy
    # else...
     # choose the feature that maximizes the information gain
     best_feature_name, best_feature_id = self._get_feature_max_information_gain(x_ids, feature_ids)
     node.value = best_feature_name
     node.childs = []
     # value of the chosen feature for each instance
     feature_values = list(set([self.X[x][best_feature_id] for x in x_ids]))
     # loop through all the values
     for value in feature_values:
         child = Node()
         child.value = value  # add a branch from the node to each feature value in our feature
         node.childs.append(child)  # append new child node to current node
         child_x_ids = [x for x in x_ids if self.X[x][best_feature_id] == value] # instances that take the branch
         if not child_x_ids:
             child.next = max(set(labels_in_features), key=labels_in_features.count)
             print('')
         else:
             if feature_ids and best_feature_id in feature_ids:
                 to_remove = feature_ids.index(best_feature_id)
                 feature_ids.pop(to_remove)
             # recursively call the algorithm
             child.next = self._id3_recv(child_x_ids, feature_ids, child.next)
     return node

