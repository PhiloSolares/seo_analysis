import gradio as gr
from seo_analysis_tool import analyze_website, meta_tags_output, heading_tags_output, competitor_url_input, top10keywords_output, cluster_table_output, cluster_plot_output, keyword_plot_output, seo_analysis_output

gr.Interface(
    fn=analyze_website,
    inputs=competitor_url_input,
    outputs=[
        meta_tags_output,
        heading_tags_output,
        top10keywords_output,
        cluster_table_output,
        cluster_plot_output,
        keyword_plot_output,
        seo_analysis_output,
    ],
    title="SEO Analysis Tool",
    description="Enter a competitor URL to perform an SEO analysis.",
).launch(debug=True, share=True)
