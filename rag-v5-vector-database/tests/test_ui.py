from utils import terminal_ui as ui

ui.print_header("Version 5 - Vector Database")

ui.print_step(1, 6, "Loading Model")

ui.info("Initializing...")

ui.success("Model Loaded")

ui.warning("Demo Warning")

ui.error("Demo Error")

ui.print_summary(
    pdf_name="sample.pdf",
    total_chunks=5,
    total_embeddings=5,
    embedding_dimension=384
)