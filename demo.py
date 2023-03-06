# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
from paddleocr_convert import PaddleOCRModelConvert


converter = PaddleOCRModelConvert()

# converter('ch_PP-OCRv3_det_infer.tar', save_dir)

# url = 'https://paddleocr.bj.bcebos.com/PP-OCRv3/chinese/ch_PP-OCRv3_det_infer.tar'

# url = 'https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_mobile_v2.0_cls_infer.tar'

url = 'https://paddleocr.bj.bcebos.com/PP-OCRv3/chinese/ch_PP-OCRv3_rec_infer.tar'

save_dir = 'models'
txt_path = 'https://gitee.com/paddlepaddle/PaddleOCR/raw/release/2.6/ppocr/utils/ppocr_keys_v1.txt'

converter(url, save_dir, txt_path=txt_path, is_del_raw=True)
