import math
import numpy as np

class DT:
    def __init__(self):
        self.tree = None


    def print(self, columns, node, depth=0):
        #print(self.tree)

        attr = columns[node["attr"]]
        for child in node["children"]:
            child_node = node["children"][child]

            print(f"{'|   '*depth}{attr} = {child}", end="")
            if child_node["type"] == "leaf":
                print(f": {child_node['value']} {child_node['correct']}")
            else:
                print("")
                self.print(columns, child_node, depth+1)


    def train(self, data):
        # the inputs
        x = [tuple(row[:-1]) for row in data]
        y = [row[-1] for row in data]

        self.tree = self.dtl(x, y, None)
        #print(self.tree)

    def dtl(self, x, y, default):
        #print("dtl", len(y))
        #print("dtl", x, y, default)

        n = len(y)

        # No examples
        if n == 0:
            return {
                "type": "leaf",
                "value": default,
                "correct": "(0.0/0.0)"
            }

        # All examples have same classification
        elif len(set(y)) == 1:
            return {
                "type": "leaf",
                "value": y[0],
                "correct": f"({n:.1f}/{0:.1f})"
            }

        # All examples have same attributes
        elif len(set(x)) == 1:
            mode = DT.mode(y)
            correct = sum([i==mode for i in y])
            return {
                "type": "leaf",
                "value": DT.mode(y),
                "correct": f"({correct:.1f}/{n-correct:.1f})"
            }


        else:
            best_attr = self.get_best_attr(x, y)

            node = {
                "type": "node",
                "attr": best_attr,
                "children": {}
            }

            #print(best_attr)

            x_attr = [i[best_attr] for i in x]

            # print(x, y)
            # print(best_attr)

            for attr_val in set(x_attr):
                attr_where = np.array(x_attr) == attr_val
                x_attr_val = [i for i,j in zip(x, attr_where) if j]
                y_attr_val = [i for i,j in zip(y, attr_where) if j]
                #print(best_attr, attr_val, y_attr_val)

                node["children"][attr_val] = self.dtl(
                    x_attr_val,
                    y_attr_val,
                    DT.mode(y)
                )

            return node


    def get_best_attr(self, x, y):
        """ Find attribute with lowest entropy """

        entropies = {}
        for attr in range(len(x[0])):
            x_attr = [i[attr] for i in x]

            # skip attribute if all values are the same
            if len(set(x_attr)) == 1:
                continue

            attr_entropy = 0
            for attr_val in set(x_attr):
                attr_where = np.array(x_attr) == attr_val
                y_attr_val = [i for i,j in zip(y, attr_where) if j]

                #print(attr, attr_val, y_attr_val)
                prop = sum(attr_where) / len(y)
                attr_entropy += DT.entropy(y_attr_val) * prop

            entropies[attr] = attr_entropy
            #print(attr, attr_entropy)

        #print(entropies)

        #print(entropies)
        best_attr = sorted(entropies.items(), key=lambda x:x[1])[0][0]

        return best_attr


    def entropy(y):
        """
            returns the entropy of a list of discrete elements
        """
        counts = {}
        for i in y:
            if i not in counts:
                counts[i] = 0
            counts[i] += 1

        h = 0
        for i in counts:
            p = counts[i] / len(y)
            h += -p * math.log2(p)

        return h



    def mode(y):
        """
            returns the mode of a list of yes or no elements
        """
        yes = sum([i=="yes" for i in y])
        if yes >= len(y)/2:
            return "yes"
        else:
            return "no"

        #counts = {}
        #for i in y:
        #    if i not in counts:
        #        counts[i] = 0
        #    counts[i] += 1

        #return sorted(counts.items(), key=lambda x:x[1])[-1][0]



    def test(self, data):
        #print("testing")
        #print(data)

        results = []
        for i in range(len(data)):
            results.append(self.test_row(data[i]))

        #self.test_row("low,high,low,high,high,high,high,high".split(","))
        return results


    def test_row(self, row):
        #print(row)
        node = self.tree
        while node["type"] != "leaf":
            #print(node["type"], node["attr"], node["children"].keys())

            attr = row[node["attr"]]
            if attr not in node["children"]:
                return "yes"
            node = node["children"][attr]

        return node["value"]
