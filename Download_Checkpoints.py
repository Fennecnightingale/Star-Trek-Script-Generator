#taken from this StackOverflow answer: https://stackoverflow.com/a/39225039
import requests
import gpt_2_simple as gpt2

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                
# establish all of our files we need to download                 
tars = {'1wMmNamzt6ayCYmlunLw6H1GOLgAUrEPc':'checkpoint_a.tar',
        '1K1zFCGcJqb4JIBMVCBvVI44OIsycll90':'checkpoint_b.tar',
        '1GXYzIIMrl5gFNkc785J_CalpMrn01OS9':'checkpoint_c.tar',
        '1XkEgURD-Szah-HCb-RIOK8sbla4bHX01':'checkpoint_d.tar',
        '1--orGXOjGSJpiLMBnB_nvAFUCBROAulG':'checkpoint_new_a.tar',
        '1--yrTnr5zwkec6PjeZbbdP052w8pJ9d5':'checkpoint_new_b.tar',
        '1MlFeU_O4-KlEQrIJAcSMU_TS7_ISILSs':'checkpoint_new_c.tar',
        '1oPlVpPb-yqArZMhC0jb7zwAm4ueELont':'checkpoint_new_d.tar',
        '12TSJizAfTQ8_4f1ckEItT5mXrTVHn9B3':'checkpoint_old_a.tar',
        '1Lr07Y4tii8DcUJdM8U1qUtq-_MEFwZz1':'checkpoint_old_b.tar',
        '1tTalGyoIUF43yqUtNxduOXKLprI_UKi3':'checkpoint_old_c.tar',
        '1ETCmmrZ97Woscxe7sf-BQFyB9PM92rc7':'checkpoint_old_d.tar',
        '16mB9ZCBSBT79lNIh0icGbSGgduJ1JXzI':'checkpoint_TOS_A.tar',
        '1OhFVPxMJ9hKuBd9dTZ1mlA5wXh1WcqCp':'checkpoint_TOS_B.tar',
        '1KlCnvWEdWJDvhp_6G4VIKvbPpqiWodgM':'checkpoint_TOS_C.tar',
        '16LpMbYwuv-TvyD_LK71STXr21rm5XGVm':'checkpoint_TOS_D.tar',
        '12OYCeAFjGY3xfchIjfIwIb1XYZoBXp2z':'checkpoint_TNG_A.tar',
        '14d7NsTLHTdNZ8rWDTjuQIEI7oic8GyaT':'checkpoint_TNG_B.tar',
        '1YH6bZPKVpRPb_p1LhiJwO3MWjUs95nLj':'checkpoint_TNG_C.tar',
        '11dghqLE4Hf6qiEgnEFxgQqmDGh2joYEz':'checkpoint_TNG_D.tar',
        '1ZRkXc8fwBOTypXEJA1ME32_4TZL0c-Pp':'checkpoint_DS9_A.tar',
        '1-4s3Kn7-zgvzs7-4No5dvyFd1eYK_-E_':'checkpoint_DS9_B.tar',
        '1mWat8pPAEK9ayiOfZ9dXrfFlvO1y89so':'checkpoint_DS9_C.tar',
        '1XcwNKxNjyrdzwC07MM-TLCZzEZT7EdoE':'checkpoint_DS9_D.tar',
        '1-1BPcmPoSQtduy_QYhX5-gtg62FR4BH3':'checkpoint_VOY_A.tar',
        '1-0dfi-CYUUUY_T2Z5usrzIJ4CWfz1bLD':'checkpoint_VOY_B.tar',
        '1-AcQeD44bn5lf9gA9iAFChqYHY5Ty7Eh':'checkpoint_VOY_C.tar',
        '1-1kL3v9ILzg6Sq_atHavz0_OEIJNjFF':'checkpoint_VOY_D.tar',
        '1hBXXaMCAchQ71HdC24rDxFMPaDklPgWD':'checkpoint_ENT_A.tar',
        '1-0qyvxL514BDI-qY_jZPt65xg2AE0s8R':'checkpoint_ENT_B.tar',
        '1--Kj0Lk1F91mwtcq42Ydv_mQsRuTw0Tw':'checkpoint_ENT_C.tar',
        '1bh7sgZT1wrbEEezNUrg5PfPDZoJUquRb':'checkpoint_ENT_D.tar',
        '1--p-vPF_iHOloHLVKgDL4x2jTZ2FJEkj':'checkpoint_DSC_A.tar',
        '1-2I9ySHjTU6S1nauwKSXg8hSidCcWLWj':'checkpoint_DSC_B.tar',
        '1-1HPkrtV_zToW7EQtrxSZglkKbOKtH8D':'checkpoint_DSC_C.tar',
        '1-6zH5veUpsmZ18zMgPCvTVwuCAglmDbr':'checkpoint_DSC_D.tar',
        '1--6l_HLYxXqmfqDNN3zj9IxJmrQ8grxv':'checkpoint_PIC_A.tar',
        '1-0sMMfbRp_ETwPnFinb10QUrXf6ZU5lE':'checkpoint_PIC_B.tar',
        '1-0fBFT6e_fXpipIh_17blYNC-vHtrakB':'checkpoint_PIC_C.tar',
        '1qbE7XbSywcis9gHlY8TWiAFjkXt1sN5M':'checkpoint_PIC_D.tar',
        '12uifxl-nbOpt-WgsUD2bDRsUMLCF1uUm':'checkpoint_LD_A.tar',
        '1-1JLEVoKUXtPKCTQSSm8DkvFz0I5rNrI':'checkpoint_LD_B.tar',
        '1-7YVf4WKgVU9n28KNdSw76f10ESz898p':'checkpoint_LD_C.tar',
        '1-8KUVby2MtST3ZwS2TikwP73z2jiagVT':'checkpoint_LD_D.tar'}

#download everything 
for tar in tars:
    download_file_from_google_drive(tar, f'tars/{tars[tar]}')
    
gpt2.download_gpt2(model_dir='models', model_name='1558M')