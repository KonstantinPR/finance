from io import BytesIO
import pandas as pd
from PIL import Image
import openpyxl
from openpyxl.worksheet.dimensions import ColumnDimension, DimensionHolder
from openpyxl.utils import get_column_letter


def io_output_txt_csv(df: pd.DataFrame, sep: str = ",", header: bool = False, index: bool = False) -> BytesIO:
    output = BytesIO()
    df = df.to_csv(header=header, index=index, sep=sep).encode()
    output.write(df)
    output.seek(0)
    return output


def io_output(df: pd.DataFrame) -> BytesIO:
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer)
    writer.close()
    output.seek(0)
    return output

def io_output_styleframe(sf) -> BytesIO:
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='openpyxl')
    sf.to_excel(writer)
    writer.close()
    output.seek(0)
    return output


def io_img_output(img: Image.Image) -> BytesIO:
    img_io = BytesIO()
    img.save(img_io, 'JPEG', quality=100)
    img_io.seek(0)
    return img_io

# def io_output_all(file_io):
#     file_io = BytesIO()
#     file_io.seek(0)
#     return file_io
