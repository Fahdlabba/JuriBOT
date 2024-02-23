import pydotplus


myplan="""digraph { 
            Importing_the_necessary_Libraries -> 
            download_arabic_trained_data -> 
            get_Image_from_user ->
            read_image_by -> 
            preprocess_image_by_normalize_it -> 
            generate_OCR_Text_by_pytesseract ->
            preprocess_text_by_remove_special_characters ->
            pass_text_to_Gemini_LLM_and_Extract_Information -> 
            formating_the_Information_To_Json_File 
        }"""
mygraph=pydotplus.graph_from_dot_data(myplan)
mygraph.write_png("pipeline.png")

