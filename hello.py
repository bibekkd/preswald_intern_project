from preswald import table, text, connect, get_df, slider, plotly
import pandas as pd
import plotly.express as px

text("# Game And Grade Analytics Dashboard 🎮")

connect()

data = get_df("gameandgrade_csv")

data['grade'] = pd.to_numeric(data['grade'])

selected_grade = slider("Selected Grade", min_val = data['grade'].min(), max_val = data['grade'].max(), default=50.00)

filtered_data = data[data['Sex'] == 0]


# table(data)
# table(filtered_data)

table(data[data["grade"] > selected_grade], title="Dynamic Data View")


fig = px.violin(data, x="Sex", y="grade", 
                color="Sex", 
                title="Grade Distribution by Sex",
                box=True, 
                points="all")

plotly(fig)


melted_data = data.melt(id_vars=["grade"], 
                        value_vars=["Parent Revenue", "Father Education", 
                                    "Mother Education"], 
                        var_name="Category", 
                        value_name="Value")

# Create Bar Plot
figOne = px.bar(melted_data, x="Category", 
                y="grade", 
                title="Grade vs. Parent Revenue & Education", 
                color="Category", 
                barmode="group"
        )

# Show Plot
plotly(figOne)

figScatter = px.scatter(data, 
                        x="grade", 
                        y="Percentage", 
                        title="Grade vs. Percentage", 
                        color="Percentage", 
                    )
plotly(figScatter)


figOne = px.box(melted_data, x="Category", y="Value", color="Category", 
            title="Parent Revenue & Education Distribution",
            points="all",  
            hover_data=["grade"]
            ) 

figOne.update_layout(
    boxmode="group",
    height=600,  
    legend_title_text="Category",
    margin=dict(l=20, r=20, t=60, b=20)
)

# Show Plot
plotly(figOne)


fig = px.scatter_matrix(data, 
                        dimensions=["Playing Years", "Playing Often", 
                                    "Playing Hours", "Playing Games", 
                                    "grade"], 
                        color="grade")
plotly(fig)


