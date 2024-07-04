from pyecharts import options as opts
from pyecharts.charts import Tree
data = [
    {
        "children": [
            {"name": "B"},
            {
                "children": [{"children": [{"name": "I"}], "name": "E"}, {"name": "F"}],
                "name": "C",
            },
            {
                "children": [
                    {"children": [{"name": "J"}, {"name": "K"}], "name": "G"},
                    {"name": "H"},
                ],
                "name": "D",
            },
        ],
        "name": "A",
    }
]
c = (
    Tree()
    .add("", data)
    .set_global_opts(title_opts=opts.TitleOpts(title="Tree-基本示例"))
    .render()
)
if __name__ == "__main__":
    from fuzzywuzzy import fuzz
    print(fuzz.token_set_ratio("Sample ID","Sample Id"))