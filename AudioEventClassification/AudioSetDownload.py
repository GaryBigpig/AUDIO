
from pytube import YouTube
import os
import shutil
import math
import datetime
import youtube_dl
import csv
from pydub import AudioSegment

import collections
error=[]
def read_file(path):
    f = open(path, 'r')
    reader = csv.reader(f)
    # for i in reader:
    #     print(i)
    return list(reader)


def get_second_part_wav(main_wav_path, start_time, end_time, part_wav_path):
    start_time = float(start_time)
    end_time = float(end_time)
    start_time = start_time* 1000
    end_time = end_time * 1000
    sound = AudioSegment.from_mp3(main_wav_path)
    word = sound[start_time:end_time]
    word.export(part_wav_path, format="wav")
    return


def download_youtube(yt_id,path):
    # def download_youtube(yt_id, start_ime, end_time, path):
    # print(start_ime)
    # print(end_time)
    print(yt_id)
    url='https://www.youtube.com/watch?v='+str(yt_id)
    # url ='https://www.youtube.com/watch?v=-geVmY-Zo3E'
    # url = 'https://www.youtube.com/watch?v=JultKcPcKjk'
    print(url)
    # video = YouTube('https://www.youtube.com/watch?v=JultKcPcKjk')
    try:
        video = YouTube(url)
        video.streams.get_by_itag(18).download(path,yt_id)
    except:
        error.append(yt_id)
    # video.streams.filter(only_audio=True).all()

    # ydl_opts = {
    #     'format': 'bestaudio/best',
    #     'postprocessors': [{
    #         'key': 'FFmpegExtractAudio',
    #         'preferredcodec': 'wav',
    #         'preferredquality': '192',
    #     }],
    #     'postprocessor_args': [
    #     # "-ss",start_ime,"-t",end_time,path+yt_id+'.wav'
    #     path + yt_id + '.wav'
    # ],
    # }

    # ydl_opts = {
    #     'format': 'bestaudio/best',
    #     'postprocessors': [{
    #         'key': 'FFmpegExtractAudio',
    #         'preferredcodec': 'wav',
    #         'preferredquality': '192',
    #     }],
    #     # 'postprocessor_args': ["-ss",'0.1.10',"-t",'0.1.20'],
    # }
    # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #     # ydl.download(['https://www.youtube.com/watch?v=JultKcPcKjk'])
    #     ydl.download(['https://www.youtube.com/watch?v={}'.format(yt_id)])
    #     # 'postprocessor_args': ["-ss",'0.0.2',"-t",'0.0.5'],

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # download_youtube('https://www.youtube.com/watch?v-Nqc_1GuY3dw')
    # download_youtube('JultKcPcKjk', '0.0.0', '0.0.10',
    #                  './data/eval/')
    # meta=read_file('./meta/eval_segments.csv')
    # meta = read_file('./meta/balanced_train_segments.csv')
    meta = read_file('./source_meta_data/balanced_train_segments.csv')


    # download data
    error_list=['-2BgBBrHJkA', '-2qFJYKnruc', '-52fg-wpTtc', '-BOEJc21cD0', '-CGTSlbDU30', '-EF1Wx_W5k4',
                '-F5paNmlgEI', '-JE4GYS63ak', '-NEW4CVyCXo', '-WndEqtjsvk', '-eSwEejvFqc', '-gb5uvwsRpI',
                '-gfpYcCHGlM', '-hX9W86Ksvk', '-wMFgnGcIms', '00GZHSXnKhk', '03lZuPyQwCc', '05VYfTOuMq0',
                '05ce3SONTqI', '0H7htxFpJh4', '0NkiuHNcBEs', '0dyfl-736FE', '0mwPjBQ1inw', '0snDoWbPrE0',
                '0vo0Wt-kAuk', '0xo_z8KR_pU', '13EPAsZcqps', '1DOYARo3Dwc', '1FPGv3Gq45A', '1FTIWvkJx1I',
                '1RZFMJ_YgGQ', '1ZxLZG0gYXU', '1hpkOS9z3f4', '1lJXqptoQik', '1mmmD1khY8A', '1oxZj5KH7RM',
                '202N45_Lhn4', '20qsw7C_LM8', '25Comaspgrc', '2GNSiLWVgyk', '2LskPqwPsvs', '2MHFg67EOWs',
                '2NZJIgd8zy4', '2PE5LzmyNhk', '2VXanLrOxsE', '2VhWd0InWyI', '2VoxuYia8jA', '2dYget65VQE',
                '2ifIiItkGEo', '2klikTomtMw', '2mDtvJCnIDU', '2nLPkozoJoQ', '34B5n63bnDc', '34qgZG-4H34',
                '3DhhUOkKoY0', '3TuLGvXm85g', '3fVIahkLz-8', '3uk0Z0ET7Ow', '46tutoqsxGg', '47WfQjziZUg',
                '4FJDhRxW_nc', '4ql7qb0uL14', '52eEdZI__J8', '56KXu_uvvG8', '57ommbIaofQ', '5AutSwQw3VQ',
                '5G1ScDu7glo', '5YK3WTR_O0s', '5cVwzQZqgGU', '5kKAWy5NkOc', '5lHxZy_7NX8', '5sXeudXZJPw',
                '6-u3RAxR14Y', '672-TXEecTI', '69k_Nljn7Ks', '6M45wCmePP4', '6OfUEP8EFRM', '6c-9TWOE8mQ',
                '6krQSolZIi0', '71x6W3b-ark', '7DQOkSRUAeA', '7H8SEbiHC5s', '7JD8chF_SJY', '7PvkX-v05Dc',
                '7QxcykJSayc', '7RFHhAEb2Kk', '7Rb4eZ_P9-M', '7Su-OQMvOpc', '7VnqKF5Mhtg', '7ag2YQ1Kn2c',
                '7ckJRi8r4mA', '7eZVRMEPI1k', '7qJVCHlp0eg', '7r0NonCqIQ0', '7rgvE0EIei0', '7v9DXLv2zBY',
                '7vgdo_d23XI', '7vzasj62sUE', '7zo4ICHU9C0', '8-MsDVH3uus', '81DxjcSmeRo', '86ZOEyRCxwQ',
                '89WZKIjpqYc', '8Gm6JPyHNe8', '8HH9q4ogr7M', '8L3Qfgf5rPs', '8LKaEGUJCnM', '8MLyXIN6baA',
                '8PR96huLxpE', '8Q9URfjpCcs', '8T6y5Yr_sZo', '8WF4WNRwIp0', '8YpLhSiec4Q', '8dUQ8FQqkDo',
                '8ddIn63YZ_0', '8hCqEwEzkfM', '8ishaG9pyMA', '8l0BgXqsHLY', '8n9WjxBbp7E', '8qh4C-Tb75Q',
                '8qi4Kd67Ft4', '8qsjlzvgaZM', '8u_hYo_DTnc', '8vwATAGQuOU', '90-pPkQx80E', '91LGQOllea0',
                '94lc2zbR2Mw', '988FhRN-vM0', '98qtHYyHxz0', '9CJH-JdH4Vg', '9F6RsvNM0qc', '9L-_-lQEqyI',
                '9M3c12Fl3Rw', '9RMLTsCWqyQ', '9RTmwbSX4t0', '9V1CyZ_I9R0', '9VJszLM1lv4', '9Xmry-ckIgk',
                '9aRZuuL1JfM', '9arAFaTWBL0', '9bM_mkoP3lw', '9cW--NcKqI4', '9dg91_16cqM', '9diANFOTIiI',
                '9eeuSij6ii8', '9fL3bNArxmc', '9fvJeyH-4II', '9gRl6QmjVaU', '9h4kAH3StmA', '9jS9SPR07Fk',
                '9l2a3p3j8D8', '9lLD2OEXQGU', '9lSbs0oIZMg', '9npEh0yI-8Q', '9nz5P7qOP4s', '9oQy4X7oqjQ',
                '9rz7UC4h1PY', '9sER6dZGl0I', '9toH1_1iZO0', '9uL1FNGA9vM', '9v88NFFnt6g', '9zN50tiq2cU',
                '9zWZAdcHYTA', 'A4Jq0eN9fSg', 'A9DAEP1e4po', 'A9S3oxaothg', 'AAeYfwuVdsU', 'ACOHx6UdtVc',
                'AJHIsvmXGaQ', 'AJpUGLilIqI', 'AMDTGkpAYFQ', 'AMGVoJJfWL4', 'AOkOMWXRdzM', 'AS-lu9HCu60',
                'AUKrgZPP3IA', 'AV99tsJuB-A', 'AZ6YVWsmYWc', 'A_fcJiewJbw', 'AcCJCJrtn0U', 'AeBKGoECU9E',
                'AfigIBp0mLU', 'AgUlAqUly1s', 'AgcKW5ltEgo', 'AjCji96erAc', 'AjQpqRcpG4E', 'AkSH1RjF05g',
                'AnDbC4puNyQ', 'ApxHPA1jL4k', 'AsR9GUzVsqg', 'Aua7vQ4MkVU', 'AugC8T-8nGo', 'B066YDLDvh0',
                'B1QjjHQCDiM', 'B4_ruAnPGFc', 'B6jMO3azBJU', 'B8A9GJPu2TM', 'B8jduAA_GyY', 'BDjW0aQKIRQ',
                'BDzHuCPySrI', 'BFnWuw4dAGk', 'BJeJZ6FzmeQ', 'BKPbQ2GWJZ0', 'BO5MJAZ6fso', 'BU2oNdqxYBQ',
                'BWyGs_EeEXs', 'B_JhDsbO3go', 'Bdez-Sk1zQo', 'BeK-a7tCUvE', 'BhG25e3s_F8', 'BowtJ6RFSvc',
                'BrohDjf-DtA', 'BswpbjoWjRw', 'C1orXgmSwQ8', 'C2FttgsUlxE', 'C3gtpClbp8k', 'C4funUEjEM4',
                'C7psbpRep4w', 'C9tM5NEoCAQ', 'CC8ZYGk63W0', 'CDClgRElouk', 'CFhHgIMVUW4', 'CKaM6h11rJg',
                'CKiXwtIFMKY', 'CKomName1z8', 'CLhB1j_4QKY', 'CMwg5-CZseI', 'CN3nSRQFKmM', 'CN4DcBT9WcE',
                'CSbW4t0TY14', 'CUF2OY36IdA', 'CUImTjOytBY', 'CVE_qMz6To8', 'CYExIUg4q_Y', 'CYlnZIMmRBY',
                'CZRqJ_QxFt4', 'C_x8cWnP-_M', 'CaZcvA2xjYE', 'CauQnOeuO6A', 'CdOBR5tTosY', 'CgPpc2uE3V8',
                'Cn4uLjSUFa8', 'CpilfS-33aM', 'CqR02tYs2EY', 'CtgkXz89HYE', 'CxduHXC118w', 'D0Q_8WBkHPk',
                'D18saDdGvsw', 'D5ffKGoOdmQ', 'D60kWZC4wcw', 'D6Xvd2f98Qo', 'D6slIrBwS4k', 'D7a5QMGqQUY',
                'D7xjedYUX6g', 'D8TCZl8TLwM', 'D9D7cU_N1J8', 'DBMuhDBlqP0', 'DBu8o3Bk0S4', 'DEBQP_oG8y0',
                'DFs79nw0JGk', 'DHpIGMIub70', 'DHw7yJIKIOo', 'DJ8rJ4PmBLY', 'DMMWeO9J_-k', 'DOTXOWAGNDg',
                'DOfXUjzETD8', 'DUfww-VAuFI', 'DUlqHdaW4jc', 'DWDUYINVU4k', 'DX57rZU9kYs', 'D_q4Y-rI5s4',
                'DcLH7D3EdcM', 'DdiIdDTQKck', 'DeM8Tar_sdA', 'Dgagk63cULE', 'DjKNT2uXRWU', 'Dm1Zlkp0nHg',
                'Dmo-xakLG2c', 'DnByZlF9NAE', 'DqAKqLiIwBs', 'DrjZDn3EgAg', 'DvdnW2Vo2nM', 'Dw5K1MuW7xo',
                'DxFv2wPrqUg', 'Dzj3BUEptMU', 'E6C-3XVCmfk', 'E7uu7ubPB08', 'E8X7XZ_iVc4', 'EB9uEdLTlmk',
                'EBOVeQJm2jU', 'ECwdc-7Z5IY', 'EDiVA-_vkhA', 'EDtiRUynhlA', 'EFVOYvXUmP0', 'ELeyi3cY17g',
                'ENWNe64RqFY', 'EOd7XiOOoR0', 'EYs5Q4ciu0E', 'E__SrkG0dvQ', 'EbmegDnMhEw', 'EgPIH3GAinc',
                'EhWhfCk1hSk', 'EhxFeb0nHzI', 'Ej9qnuln5-g', 'EnXcm9_68sc', 'Eq-Ahsp_cLw', 'Esjaq1m8KQk',
                'EthFkuz8oG4', 'Ev_pYJvt3dY', 'Ex2ucfMwrmQ', 'Ex7Spj_cx58', 'Exw5uDiyFow', 'F-G_B_MneGo',
                'F3D_5aRjXZ4', 'F6XcQC-M7EE', 'F9CjKPrOkk8', 'FAYRXclSJE8', 'FAxp_rtSWy4', 'FFUmJaz9740',
                'FKX5ZnFvVbc', 'FO6vMUCnZSg', 'FSBv5aVbU4c', 'FVv3FAaApwg', 'F_rkgjQKtw4', 'FbQ3R9GLv_w',
                'FdhMTY54KoM', 'FeCfebzrwpo', 'Ff8FzMxTmPU', 'FfncwUZVvjs', 'FkWSk7C2t-M', 'Fu7_ITo2Vn8',
                'FwoD5-_7QqU', 'FzmFFjxyd7w', 'G-M8RQDTosM', 'G0iSJBAVvh0', 'G15XPBRsMJ0', 'G2FStAlrF1U',
                'G4jPkInxjHE', 'G5l34WF2FeU', 'G6UODYAOZ4s', 'GAslx43jmWM', 'GBT4FiA9Wn4', 'GIWovNkYaVA',
                'GIrVnZXUgro', 'GIunOeFrZh0', 'GMqftVa3kwk', 'GRTS2czOWdk', 'GU8g59LWu1M', 'GUbb5IB45H4',
                'GVatVXEHXdo', 'GWVfJiUrSJg', 'GYmXGWEZhOo', 'Gdmms4b-yAg', 'GhMB_TNxJ2Q', 'GoTbmRD-86Y',
                'GpYx4VydZPQ', 'GpuwgwtMvfI', 'Gs5B-PtJl6Q', 'H-azB-9UeF8', 'H6JptdqRo60', 'H6NnC_hEMy0',
                'HBf_NV9FafU', 'HEPvh25dmCM', 'HG6Tesw7cM8', 'HI-2Ji_nDhk', 'HJXlM9YHAfU', 'HN44iil7vig',
                'HNlMMtbZSWQ', 'HO-B1pQCyXw', 'HOZ-AlKOom8', 'HP4pdYya5YA', 'HP7QJozYWmc', 'HPCvWIRYkYQ',
                'HQpgkH2xGPg', 'HUGjHAOZoXw', 'HWQoxySBNWk', 'HWtFkaZwOMY', 'HYmhzkfw8D4', 'HZlKKLKqiS4',
                'Hc8ncYid3so', 'HfK5FInvv1o', 'HffskAx8p0Q', 'HgPEJDHIj5Q', 'HgywJmsdGLU', 'HhVamNZmq0Q',
                'Hm-VgQC12T8', 'HmNoK7fOeGI', 'Hpn0oLqNRiE', 'Hr7WIkOL_pU', 'Hw_p5rCIUbY', 'HwkumGeO4q4',
                'HxlsfoSrHZE', 'I2PMVC-clSI', 'I4jtC7WJdGo', 'I52vIPzjsEM', 'I8XTu6CWxYg', 'IE2MjjzhuxY',
                'IEDVIMtJJIM', 'IHojOwrlup4', 'IHplK2PQ0wg', 'IVHZQa24aL8', 'IY-_OLE45tM', 'I_NNIyV408E',
                'IdenFdkeASo', 'IhmoYit4yW8', 'IiLnbYq0NRc', 'IiZ3mFhN2oA', 'Ij0NS6eNb_c', 'IltLBXPsoBQ',
                'IrTzgixFEuQ', 'IubPt0zWujs', 'IyhHrT-pWf0', 'IzDa2ch2Huk', 'J-xN9kohVks', 'J0fssLQGlQ4',
                'J0k9JgbFN_0', 'J1E9KD0o7ak', 'J6HlnT4I7bA', 'J6IrtAkUhHI', 'JElmgfGyQew', 'JHIOh8nE0WQ',
                'JIGVl0bSro8', 'JMdO23mNIlo', 'JQAI05Gt3hc', 'JS7l6HPdG7k', 'JSObWWftORo', 'JVR-DZn22_0',
                'JVwH5vhrMpM', 'JYyBeQo_gF4', 'Jc57snCLugw', 'JebIyUVVlcY', 'JnRKYE3OkSk', 'JoFetPhqQV0',
                'JofxPryZr7Y', 'JsfKfHEHHfY', 'K-WUs96xY7w', 'K4Oqo40UEEs', 'K6FRnwR1Jso', 'K9r_Apudm9s',
                'KA5dmuIUb_s', 'KCR3YK-Arzc', 'KDzawV6B1vU', 'KMixx_7pW8Y', 'KPKaOU85Dv0', 'KQEcr84bTvk',
                'KUZxIFzEXwk', 'KYL1fiUMOlQ', 'Kb6ApX3jokw', 'KbRftt5myc8', 'KcLoytYGd-A', 'KdDGn-fzzgY',
                'KdtbN8PFjDU', 'KfB0PXBxSVw', 'KgCCkdfKmLI', 'KjVJX52iCo4', 'Kl1ZbG6GmeA', 'KsHcnQvdrqw',
                'KunhpKbZH_8', 'L-s8W-SGcdM', 'L44eFQzykY8', 'LCCh88BKNsE', 'LE-E3DTf2qk', 'LJJZMPvmxvM',
                'LLam57BWQKM', 'LTJJqIPPxi0', 'LV7RYEyyNSA', 'LWEPj69H4bE', 'LXZmEHSWXmU', 'LZEnZ3I6NqU',
                'LmFYo8STHdE', 'LpKom6E4GV8', 'LpU_9DdKbnc', 'LpdXD1zX7kQ', 'Lpqgh0F8INs', 'LtcTR0hDD10',
                'LwPaKzdQX8s', 'M13ioxSrkEU', 'M1DmydIilZ4', 'M1n5rVvaHUc', 'M5D3u9XfYq8', 'M6AsaLvOOrg',
                'M6Rs3duqnx4', 'MEDSz2xJwuo', 'MFCEDh0tpSw', 'MI-cEBb1Kcw', 'MKdaH2OCke8', 'MO_Bdw3YHJ8',
                'MU0q2ev4b0o', 'MVA0tigK_oE', 'MW4LBPrcHy4', 'MXcqvmJNPso', 'MeIR02Do91w', 'MmewiFAFJ7A',
                'Mnqq-MzIDaU', 'MoyaAYkhhuU', 'MzoYW9vwRdE', 'N-QHJQQuH_4', 'N-Vhsp6tXMU', 'N0TkGUiwm8I',
                'N1c0QQXT5wU', 'N2et7A16Iz4', 'N3aVIDJefI0', 'N7RTZnFt9pI', 'N9qTmUB63A0', 'NBfkqIPP7wM',
                'NEJuIjAq2ls', 'NEm65eK6B-w', 'NGTyyMq5lQs', 'NGaMfAdCQ6Q', 'NIYltObQYAo', 'NKMb5_sAkxc',
                'NMn-9tvzQZA', 'NOveyVFWA8M', 'NPJKWIO5mSQ', 'NV7v0bMgIu0', 'NaeFxfFwFBo', 'NbqmsXrPC9c',
                'Nbv4bThrbGk', 'Nfs98kE20to', 'Ng_qFhe061Q', 'Nn7XRMkO_fY', 'NvE-dkEiKrQ', 'NwISV0dGIQE',
                'NyesN6GF_08', 'O-EvuXaPTkc', 'O2gURtZmSFs', 'O5hrcIcJ6lQ', 'O7cxuQyHuEo', 'O9AdMudcL2c',
                'O9MB3nJWGmc', 'O9dsUFYp7d8', 'O9vFQG_h7Sg', 'OEgDKYSYqXY', 'OHryvXvQPq4', 'OQg2pSx_e5M',
                'OQsw-HBzauk', 'ORJ6J8Od_IE', 'OT3SYsNznCc', 'OX9HvIixzZU', 'OYyyXbg3XQ4', 'OZAZsDN6aGs',
                'O_6eV4zX8Fc', 'OdsqikWQHtU', 'Oe6erT9TAGA', 'OeQmSnlxXOY', 'OiTicO257Dw', 'OkOuCrmeHkw',
                'OmaPZ4Ny8BE', 'OmcWBowAAY8', 'Omvy3ofdd0Y', 'Oq1b-6KVP48', 'OrVRMZspGRE', 'OtSBLRPDRzE',
                'OuCio2hai3g', 'P1RHRE2ROTY', 'P2Ws4iMosW4', 'P4JornVKffU', 'P6SNplRDMnQ', 'PBTPWOf_E-w',
                'PCJV3dyemB4', 'PEs1zNkvuZc', 'PGzjWbIpcJw', 'PHe_b0PM6Tg', 'PKWt8Xi7xSs', 'PLo9WTuLnDI',
                'POzbCQbOAl0', 'PTQpJ3kthXI', 'PTfkYnRM1No', 'PYar0dkZ6v8', 'PbTUZavwZvo', 'PdlmHvEOMRc',
                'PdnIuyjo0B0', 'PeAxrFZXI54', 'PgijXVt-UQU', 'PglS8m9hsb8', 'Pi3R9TBcWck', 'Pjxqp3QHdEw',
                'Pk85sa9OSK0', 'PkiSb8SPXik', 'Pm-LKw7pZ5A', 'PmkmMKHL0N0', 'Pn1W7YI8n_8', 'PpQQZV3THpk',
                'PsgXRv8hZl0', 'Pue983IxyIA', 'PwGVtMMNDYM', 'PwVY9mx7ADI', 'PzFUv1oxy4U', 'PzG_faf1Tdk',
                'Q57j_FroLAw', 'Q8OL4uW1CUk', 'Q8kpoWSkJds', 'QBAhvFexFpM', 'QBp86YGOFbM', 'QE3ypW8hbr4',
                'QEoHD7UCjGc', 'QH1OBECqfzk', 'QLbqO2rOzVI', 'QNiBnMlfT2U', 'QQoRfvBrLqE', 'QUYOfVx1k-A',
                'QVBcDRMvMzk', 'QWVMCK7wwx8', 'QZSKdTDkjfI', 'QZtYgqrjIrQ', 'Q_LxwjWYYzA', 'QbFmjsCcwNc',
                'QbXH638ZvqU', 'QcOeAej6b1g', 'Qhu4_9uOvy0', 'QiK_KonZ7t4', 'QmCBZ06UqLk', 'QzhGox1Nac0',
                'R0E6eE-Xiyc', 'R5E7LXevNJU', 'RA314-eE430', 'RBcoDi-MtHA', 'RDHd5pDWJMc', 'REzRyvItebY',
                'RGw1_y1JYv4', 'RIBa5WJgRBo', 'RICfy0_rhug', 'RIgggNO-aso', 'RMsqMhneVl4', 'RR5YGjMeEpg',
                'RTa0GdJOi7I', 'RTqVqVQInhQ', 'RaxoyUR_OtU', 'Rc2pXtCaC6U', 'RdKGdjEjwwo', 'RhUd3PzhHTA',
                'RiKUoYsOSwo', 'RkznSn57dGM', 'RmT1xvjvDIE', 'Rr7nBBOupKQ', 'RsPehzYtxdM', 'RtQsSPgpddA',
                'RvOGO2oppXk', 'RwLHO7kEwQo', 'S9UFAobwcVc', 'SDVzNfKAopE', 'SGiIMwpqKEo', 'SJC3oxaP2r4',
                'SKpli9iT1tQ', 'SLLGhJA5mLw', 'STUOsMPCUhY', 'SUnrKkmrIOk', 'SXtY8zUKiqo', 'Se0-9244JDk',
                'SeS98TJ1ntc', 'SfUTO3q7tl8', 'SjEdkriqG1Y', 'Sk2V83M0ZZ8', 'Sksf0eh0MSc', 'SpqOSWQ-oKE',
                'SqUYrh2tmRY', 'SsYq2IY7O5Q', 'Sse_zu45hPY', 'StjeR1EIv0A', 'SyrF1LBi0H0', 'Sz9JGvcu1nc',
                'T0rd7VS8_DQ', 'T6mW0Mmp41M', 'T8GMszNzpUg', 'TABzGvlqPFU', 'TAjf45TmBqc', 'TE43dEjJd4Q',
                'TEZXYVJW0K8', 'TGN3VMU-rds', 'TJQlo2s7Y4A', 'TNgsLCkwaMg', 'TPH_vrzx68I', 'TWAP2EA7WFo',
                'TWNdqlE5WHA', 'TWiXOjN2XEc', 'TYcfOi9qgyM', 'TZMie-5lh5o', 'Tc_sojS9nmI', 'TdPVET4c4NM',
                'TeGoW7croIM', 'ThNH-4bO20Y', 'TuciADQPk0o', 'TzQ4qYXflZg', 'U-y8TFjHRF0', 'U0I8skJ3CLg',
                'U2WbtGQNZOo', 'U2yDqJGP0DM', 'UAa03Tzkq-o', 'UCeykGT_J-M', 'UD1ll-r3ZDQ', 'UDDKPSdgSAo',
                'UEMS1x5luQk', 'UHaR998-glU', 'UJmrgFh84tg', 'ULS5Snuq_8I', 'UO4ZHFjfrQk', 'UP5Zkhg035s',
                'UTyBh-cH4Z4', 'UWtx1NZ4J6E', 'UZLcHhioJok', 'Ua1dfywxsig', 'Uj4WSh3ka-c', 'UkrcILbBaVA',
                'Ukw04hetA5w', 'UpKL7mmY8LY', 'Utw2UfZGCe8', 'UwXYf9AVw9s', 'UytY-qA8H8E', 'Uzn5kQ-afQ8',
                'V1BkPubEdCk', 'VA1xTqyuZG0', 'VAWH5vtzEsc', 'VAlrxn0oL-k', 'VBNFjMlTQ6Q', 'VBW2RKrjLzE',
                'VERdSi9wPfo', 'VH-Rbc9VM-w', 'VJc1ovmqlv0', 'VK5cf08weKI', 'VMOa2kyjlPE', 'VPCpYu-6VVo',
                'VUfa1M8muyo', 'VV2GeER66qg', 'VWHp-BrJvnI', 'VXuQNn1snZ0', 'VdAZ14-NDOc', 'VkSj9TO1aSQ',
                'VkvSTDGF-OY', 'VoYogisHdQw', 'VpVQSzhSd14', 'VtqlDvNSQVI', 'VzGOjcOj9fo', 'W560dJ7FC18',
                'W58c7BXsEz4', 'W8yh7zm0B9A', 'WAsayl6LjV8', 'WD8TVzDCD4o', 'WDDBngegDn4', 'WDfx209pyOc',
                'WGCF2sX6XMc', 'WIqJwtarmNE', 'WOux8gMwbDs', 'WQWkk0Itza4', 'WRO21qDSq8I', 'WRR3Dy7gXwA',
                'WVPGrUS1jWo', 'WYDUKWGg4rk', 'W_HhkSI07ms', 'Wak5QxsS-QU', 'Wau82R1pEUE', 'Wb5U7RKOT6w',
                'Wdq-ISRFB5U', 'WeRVhyGIg_w', 'Wjb0FgQqpZA', 'Wl1bOlfU9XI', 'Wn9PbVp71RM', 'WoUvK5COJ-4',
                'WrHCDT--UKQ', 'WtiOjEyfR94', 'WvjOG6N7wNQ', 'Wvw4S1V99QA', 'WxAbG83t49w', 'X24bu-DGY6M',
                'XAdaUxNEhOA', 'XEpa-JM8fr0', 'XFqjrwYMLkI', 'XHSf6GwjANc', 'XOG6UiYtGTI', 'XOLRv4YN2s8',
                'XP9kR8cSmAg', 'XQ3Bv5K5UCY', 'XXvjDrgTdE4', 'XYuC3G9RE6g', 'X_1s-v_WA3c', 'X_B3rT-XrxQ',
                'X_Q4Pp7OhNo', 'XaE_shQeldw', 'XeBd8pH3L8A', 'Xf-irFKB0Cc', 'Xfa4M12IbI4', 'XishfHZT7Bo',
                'XjGiiesddM4', 'XlUfeSK4tZI', 'Xpnhh3QfbJs', 'XqwhN6Wb_sA', 'Xs0jAd-_ccQ', 'Xs6tiB706M4',
                'XsHNO9mqSYM', 'XtGQhsKIldU', 'XwdvUn3lmQ8', 'XxfgmvkTAuk', 'Xz2UxZIjm9A', 'Y5cqM7He5ik',
                'Y69wa-8bGKI', 'Y6lkU_RH3mo', 'Y8PBbjqvZvM', 'YBDO0DmjUFI', 'YCJs-dwWEks', 'YCLEnkJaUN0',
                'YCvOvWQjUuw', 'YDgjj7o1jBE', 'YHQNMPPUyEg', 'YIi8VwxSntk', 'YIqG0C9QJ9I', 'YNyfQZb_5VY',
                'YOmDrNk9vWg', 'YRa5tjnFOf0', 'YSWiCtX74ck', 'YV2wuAimpOQ', 'YVUVbvgk6yc', 'YZS86P-gwv8',
                'YawqEEhKr8M', 'YcBetXgzYYM', 'YdVsAwi_ubI', 'YkWUz_uWGek', 'YtPLLfyzeFc', 'YtnGCZu0LdQ',
                'YwCBXxDdBL4', 'Ywc4_D3sKHQ', 'YybdU5g76Uc', 'YyqqXEmYPIA', 'Z0bHhksIC9o', 'Z1BUMF_46N4',
                'Z1CcbYOWe_Q', 'Z2mS-eY0g0Q', 'Z58kdUMRBSw', 'ZFBfhGN_Mj4', 'ZHnBiBNqqsk', 'ZMxYu5jQdMs',
                'ZNISbjG3FvI', 'ZQFZLu-D3bE', 'ZSPaqUilm9I', 'ZTBaXHPSF4Y', 'ZULVl-kzo60', 'ZdS71GVTAOo',
                'ZeEYaTFxHIk', 'ZquOZnRGwhY', 'ZxfWio8dmMo', '_-wSgg4A6Ag', '_-z5aoNwgFk', '_0iMtaBaxfw',
                '_GbpS9uVajI', '_MCvf4giiqE', '_NLWvZHkjH0', '_N_TCs2ehuo', '_XPPISqmXSE', '__LPqvWwDCU',
                '_gljd3FjRag', '_n-kUOZk0A8', '_nlaU3VUfe0', '_sPsvB0PWEI', '_uOmCK2XeaM', '_yImzbi82Pg',
                '_zQ6ux9jgAk', '_zUxoKxirkU', 'a-Kzql4_yfE', 'a1mHN4nDko8', 'a41QViamWsM', 'a6hQFPi8De4',
                'a9ajriudKt8', 'aBDNbOssq1Q', 'aByzkxBSlBM', 'aDdZN0bXDbM', 'aDy5KNcjNrI', 'aHQeamPCfVU',
                'aIeog_IkSXg', 'aKuIwxyTKiY', 'aMlyQysMdXM', 'aTO9V8W9Bg4', 'aWEsPJKHr1g', 'aZsaM0PNRns',
                'aagz3b91Wqk', 'aeXIHmz127Q', 'alVfhRuFeVE', 'al_vPe40xc0', 'altXfgbNIBo', 'alydjYAu4s4',
                'atm7KcXQueY', 'ax0pj17NwvI', 'azAdALMtEOo', 'azc9kPsxVK8', 'b-XuYaFCHlk', 'b6zTCL8cGOA',
                'b8BfZeoWDyA', 'b8Pk-F_GqPw', 'b9Gx-dw9vBM', 'bKuK6nu3R6g', 'bLB60drMM_c', 'bU5Cpbpb_VQ',
                'bUWowdixo9s', 'bUuM_QJeyDI', 'bZLzkmiHN5o', 'bbDMGICoMDg', 'bbGWW_s5si8', 'bj0ER7A8QnY',
                'bkiV2Rotkj8', 'bpyp_xK3W_g', 'br4-7Jj2tuI', 'brDslKw2gz4', 'brhKfD49cCs', 'bs2e0PglyTQ',
                'bsIV_TiGpLE', 'bv3ThYjZS8s', 'bvGOYIXgDuE', 'byciumnlF48', 'c-4EDEcHyk4', 'c1MWFFRJ-wo',
                'c2VUAdnnTA4', 'c4Im_JXFsqM', 'c5E0MDKdXdk', 'c5XhNq7wRnQ', 'c8uhOIsBdug', 'cA13fTLAdW4',
                'cHA5bgd0y88', 'cIwhCa9DuLA', 'cLwVV_f2IEM', 'cMfOecMPlGg', 'cOlrPtpbdLs', 'cRCiQnKRzEI',
                'cU9AJygC17I', 'cUzVLZypM5Y', 'cYhYBPZwD00', 'cYkV7ILQRwc', 'cZHuXolLfj4', 'c_DWukbLTys',
                'cb5gm_LXVgY', 'cfa_1bbr5PA', 'cfpuUtbZtSg', 'ciw5KOMF9tw', 'cjC84wnuW44', 'cpedkrWoxY4',
                'cryfsdaPUJA', 'ct-2hxVLQ6A', 'cuRjCW69fiI', 'cwRQHKgnUAI', 'd-5jr8OCpgc', 'd0-n3z-TYlA',
                'd1GcUbFJtRA', 'd2TwxzimnCA', 'd4sRdJnv14o', 'd5I-ze4YgMo', 'd6ex3WZZV78', 'd7j7lYqobpw',
                'd8QZMJVgxmY', 'dAK9EkX1Mjw', 'dEz4YbHEvwg', 'dFnQrwu848w', 'dIrpIm-imYY', 'dKw61xLXo8Y',
                'dL1Wk0-CoEY', 'dLdMryWLwj0', 'dOrsPLYuNA0', 'dQB_g7EMBI8', 'dXeInn2-vY0', 'dYiFalPr1xI',
                'dalb73sMJX4', 'dbcPx4R7r2I', 'dkookunC_HY', 'dmzAID-aYwY', 'dp9ymEhtaQ8', 'dpLq5xDPjnI',
                'dpwsEGAcO7g', 'drkDWFHVUVQ', 'dsmeCZOJBvM', 'dupAZBORHdc', 'dwrnbgJ2mAs', 'dzrBQnCaFp0',
                'e-0WS00pXWg', 'e1xFNcihXyA', 'e2Ku4nh-vAA', 'e4keL3T9Hz4', 'eCvXsTfjYT8', 'eHX7AP3RM1c',
                'eRtcXWNqPcM', 'eV8XidTF80s', 'eVeNIfjNSEc', 'eWDCNlQ-GOI', 'eXboOU89jDA', 'eYaoYPnUN-Y',
                'e_7_kuFlYNE', 'ecrJob5YdNY', 'ef7EjtZAHps', 'egLXbWr40nM', 'eiLxTLzqHLE', 'ejVaACsSaC8',
                'eoUb9_avYWc', 'es37q_dG7Fo', 'esLf6DPp3DE', 'euK9xaZAdZA', 'ewsZekIt9T0', 'exJlu3wvzNs',
                'ey3CPBH6Jyw', 'f-VMVT0p0W8', 'f-lsMvfBE6w', 'f60shKKRYIc', 'f7GdHA9E1hc', 'f9KdVHm57KU',
                'fMJDfk62on0', 'fPEoegZm7eU', 'fThwUtp9sWU', 'fXCMPr5Zm4Q', 'fZGXBLeQI6w', 'fawUEf83LT8',
                'fcWJXg8zK7U', 'feFJuNFY6Dw', 'fgyySe3s6aI', 'fhuufkjI6FY', 'fnFoX_fBXRE', 'fpPYEIMwlW8',
                'frCiU9anfEM', 'fuI0L8mrqHE', 'fwBvqPuzP1Y', 'fxTR34bd4nQ', 'fz7zQOT2kZ0', 'fzWJbmqBiTU',
                'g0q4auyp2kw', 'g4WvtrsgYxY', 'g7Apq0tVI7E', 'g8hiCn2lPmQ', 'gCMlVyxRPik', 'gCiArkOeIaE',
                'gEyDpOa4TAQ', 'gGeFh2qzCDw', 'gIxQmx_o-_k', 'gR3DfdA2DmY', 'gUTPqiYFryc', 'gW5gDHs9RkI',
                'gXIB6aETeLQ', 'gdEOkVNLNXk', 'geuZX67LfNE', 'gga5z7_kqis', 'ghb17tdhiKQ', 'ghz6s0fWy3Q',
                'gm6ZAFsztZU', 'gqWaDVBsPrc', 'grZlWQq40Ts', 'gsfZKUemin4', 'gtxv5vqqRS8', 'gwRujKi6B_I',
                'gwjBAjcugR8', 'gwwUsNY3ckw', 'gy6-8Zqr9LM', 'gz45mP7trmU', 'gzB2yQfd2Js', 'h1g2jAT-QyU',
                'h3XC4Cz4U38', 'h7WnOpqmSkQ', 'hChxVDbmG_M', 'hGnMaFEmR9M', 'hJhst6ZMoz0', 'hQlW5n8QlLA',
                'hWQTA85Yknk', 'hYCOh_BGErw', 'heJ2b85kb_8', 'hjEXNQNj7c0', 'hmSZAhDQyLI', 'hoZunwHnU68',
                'hp4QpHrKTfg', 'htO_4F0BzEI', 'huNWhYHiVUU', 'hvbj8tW9Epo', 'hwPKWs6q5zw', 'i2j404CU2DQ',
                'i4IsKRvCLi0', 'i4ZZgZ3AxEg', 'iBbK-joPmHU', 'iBbOgiYrZtU', 'iGv9MMaiD70', 'iJgp4YAO3No',
                'iK0CCBkGokM', 'iO_V-6iPr2g', 'iPR37Z4g04k', 'iPcZEKznnp8', 'iPdXQ7arhJU', 'iQ5lVnRRooE',
                'iQD3jqBQSwU', 'iSPKYAIMm_k', 'iW_40jBKQX0', 'i_pxccGJTGg', 'iaFR62mt5nM', 'iaYdJQiZrhU',
                'ib-j_RhDwNE', 'ic7_qCIZyIg', 'icWfjMKE0Gc', 'iiSx5bLo7ac', 'is9E_PKRnS8', 'iwEx_2oB2Uc',
                'j-0ZbuvVCJE', 'j5NQQjfTrJc', 'j5pKotkHyb0', 'j7Hzru3CLrA', 'jFWB9QVP744', 'jKiM8cAiUag',
                'jOVpnF39yow', 'jP8MINTY2sA', 'jPNrqtWorWY', 'jVvNy0CeA-w', 'jbcGNz3HUtE', 'jf9oTrasj98',
                'jfATgiJqc-w', 'jhI2rWUXaFk', 'jqW8lLjnyaE', 'k02rEqA1BO4', 'k0pygHz4-hw', 'k8B5avou07M',
                'kAbBxZBjHeQ', 'kGPbA9wowRk', 'kHBmEsJYFWw', 'kKFzoV-2AzA', 'kKPyJdphEHA', 'kPuOsK1a8Co',
                'kQ3E6A9h5pA', 'kRACDr68QZs', 'kRUynPE315g', 'kRjnzI1uv00', 'kTqM4QRmuAY', 'kVSMjlcSsiY',
                'kWBpeIHF9m4', 'kY4oaEjfxCc', 'kZJDGLRtbgI', 'kbGzpLnJjFk', 'kf20hA399vg', 'kfZMA7t-HcM',
                'kgblAHD1xAY', 'kjk-qYdgYAo', 'km3PFqxOgno', 'ktlCVoiAlug', 'kuUWgcU6MX0', 'kxiLSivpKNY',
                'kzudN5-ZNQM', 'l3JeuJDkUDE', 'l5W4NsXy_RI', 'l8bis7ntbc0', 'lBbPFaN9unE', 'lDfNstN_EFI',
                'lJRaSfQidp4', 'lJYeyCXosjI', 'lM5nxAAYcYw', 'lQJFbTtEUKY', 'lRvgrqdsoZc', 'lYNFsXqWlnM',
                'l_mlV0HST60', 'leGWsrM8NBw', 'lebcIOMH3Ok', 'lfAGIzFvtD8', 'lgF9muEpZUQ', 'lgWDit2vU4Q',
                'lhqmKIuXywI', 'lj7NcwkZo8Y', 'lmycjIsDXdo', 'lnbpzQ0Mki8', 'lnq-KpZSZTw', 'log-H156Mr0',
                'lrIXmX_p_94', 'lvKPNGO435g', 'm289GfGiqi4', 'm2yPxziZyN4', 'mD4ed7LDTqQ', 'mG__E6XYauk',
                'mHbWqkCK2EA', 'mKeLOPmevJ0', 'mM-VW-h7reE', 'mScCmpfJNzM', 'mSxEjj_Izow', 'mURLfUf6keY',
                'mW5Lu55f8oM', 'mYabjBQaFaY', 'mZ3eJOnozHE', 'm_NCf-q4Gn0', 'mcAl7ILPMwg', 'mh7rDFB3DMw',
                'mhFVPYPmNVY', 'mhwuZTe5jIo', 'mijkRd8cBjY', 'mjkBbCiDMls', 'mnKlXq9Lo7k', 'mv4G9boO-4U',
                'n3yvCCDh1L8', 'n6MpuAuT6E0', 'n7f8Q82T1tI', 'n88LbL3fHWI', 'n9MceWXzRQM', 'nEDnXwXRtag',
                'nHrrpEPBJ7k', 'nI78XK2qRbM', 'nJ3hNN0nD6I', 'nKG5K7j5mlI', 'nLBbG4S6qWk', 'nSEu5okfhG0',
                'nTtwLPB3wt4', 'nXVJmgQyv2c', 'nYGEsnOfqFo', 'nZqaiDLQWD0', 'na0zJA_YevE', 'ng7X2FBuCpE',
                'nje3djJuQu8', 'nkakGceIXrs', 'nmB7GieiiHw', 'nqe7A4IQmXk', 'nqu4ATfNugs', 'nv3FzXZ2s2s',
                'o-incQgeoEo', 'o0wO84MNVGA', 'o2jT6rzCvqI', 'o7fJyOilNBY', 'oBGAnBBhLKQ', 'oGMJH79bF_g',
                'oQYyHcIxrMY', 'oSlyf_q9Ffk', 'oWM3UjJaRpA', 'oYKuNlcqCSk', 'oaBxmlrnFTw', 'ob1x9dh84Kw',
                'oezAMNywotU', 'ohKDZ9zrW28', 'ovd2Fk4JWXo', 'oveJDfNxcA8', 'oxOyoH707Yc', 'oy-ZMaQbe9c',
                'p4n3wWpcNPs', 'p6fPGXSh3pI', 'p6lx1ozL-tM', 'pCBP6_uprCA', 'pDFrCpRiJ-g', 'pDMKqfjviVo',
                'pI5SCG6oPhM', 'pLv7XqdKoBA', 'pNnc67YhnQo', 'pOymTBEyJcM', 'pQrx4UMW-Sg', 'pRlWXA5axBE',
                'pSJxQlSNDAU', 'pUoQb-bm-FU', 'pW9LF_8ZTUY', 'pc0bxLn36TM', 'pce4bFCyMa0', 'pk__9yJTu5w',
                'pkab4C1Hvks', 'pm6deQb1LvA', 'ppUhXhseu0E', 'pvtauHBAvUE', 'q0qfWupr6SQ', 'q3K43BgzqWY',
                'q43gH9B-CYI', 'q5FwsIkJCXU', 'q6BraeGmvxA', 'q6M54oE33QE', 'q6rIMIO0zt8', 'q7s2qM42CQ8',
                'q8rtxK-WkCk', 'q9Ta3pztAEE', 'qBeXiWSx4gE', 'qCp6qinqyrY', 'qD7yyQ7a7W4', 'qJT4cbLVFuw',
                'qMcDbKF5Hjw', 'qPTwqnfPQvA', 'qW7h3PZqFlk', 'qWxvvNXnfFU', 'qbpljVsqw9Q', 'qcbkfcAYX50',
                'qd6KQfWMcd0', 'qoi38xLdVVw', 'qwTwLLs_FrQ', 'qwdDbxYIhnw', 'qygzCLUnqlM', 'rGB6DoOhqzE',
                'rNA9obsPFJk', 'rR5ogyX8-MA', 'rSu1Cr43S2s', 'rVtzhmRzotI', 'rdK8Q-r8EYc', 're37z5rMIsY',
                'rhrNqhaH6jc', 'rj6DfaS-e38', 'rmX7XBEohvY', 'rpnrfsGwwUk', 'rzQdg4wRmxY', 's-_CH7hCJfc',
                's3Ft4j0Oa44', 's99NSQWS_OQ', 'sArGQfiV2Ro', 'sCge-CzawLc', 'sDHs6f4iSfs', 'sDxrQ0_5Pek',
                'sLYYpYaBSjg', 'sO4r1jGLaPg', 's_U-3ukF_fg', 'sagXGyvabYE', 'sar__TZJPII', 'sb7XJxQ6T48',
                'sc1N841K2hY', 'siHkuDOwlrM', 'sm2TBWjWTSM', 'sqr-mVNXDFM', 'srAR-X0EfFk', 'sxhrG3uvQiU',
                'szFUyYez5Hk', 'szOPoim44rA', 't1YjTRjWOGo', 't312hrd8hL0', 't385F1Xp_-4', 't4POpKL5wVA',
                't6rniZNuoM4', 'tAm4WJ7OTYo', 'tC7qG_Kxe54', 'tCOhImPRW5A', 'tGw-y6n4ECc', 'tJG9KwyBWM4',
                'tJy0gqFIEc8', 'tKc-Qwj9aG0', 'tMSDnzpd694', 'tUfblh84MAI', 'tX7xi3XV4Fw', 'tXX2m3qu5Zk',
                't_sU_7EDjBw', 'tfjoaC5tsxg', 'thQ3PeqyArg', 'tjy66MTvFJk', 'tlSuLvSQqmI', 'tm01wPNIMhs',
                'tuiNDFOiKMA', 'u1I4dVt0nc4', 'u1a_y3Hdgug', 'u35fa-4uHQQ', 'u7kazqtJGjM', 'u8JmK2TmnEQ',
                'uA-dz_M_5Rk', 'uB_yrWtCsak', 'uC32VygDRnk', 'uDqYxW4Zjb0', 'uElyzUu79Ko', 'uInW3Rb5WsA',
                'uJta3XuHyFo', 'uKIdY6Bf8NQ', 'uOXSr0bbJHk', 'uPRgkuvf9T4', 'uTE3aZWI1vo', 'uTphX4__jEo',
                'uW0LRcK_iSU', 'uWIWnL414Lo', 'uYqRLrghziE', 'uZO3MRbD4wY', 'ua2VHkz2T0U', 'ubHxSr8gpXU',
                'ubiZGaPAarA', 'uctSYnCMwZY', 'ud3YDhmxiGs', 'ud_Cp2ZRTzQ', 'ufO5XSBVS-k', 'ujFf8dufwBc',
                'ukkNKGQbw24', 'unADFFVmEFo', 'unMlXpbpAR0', 'unjhSQnuExc', 'utrlD8tJT9k', 'uvLlgT5mwF8',
                'uywF1JafL-k', 'v2mD5eH8hgA', 'v5UlSsnmsSs', 'v7b8eL96wAg', 'v9ZOT0b7-Os', 'vAMRmYu2mXc',
                'vB1KBizUCoI', 'vCEBz9QIY1o', 'vFhkzXiX5QA', 'vHb2P8wcpMc', 'vILK2Sz4mX8', 'vJEuGVIefu0',
                'vK14LFmYYYY', 'vK8LBGUJjgw', 'vLG-3YvgUKU', 'vMD8HeOqsqU', 'vOEF-FzwSlM', 'vV2ZL7_TOpg',
                'vZxl7mo9eUM', 'v_RgNLI1rYY', 'veI1INgxkZY', 'viCVoBi16sI', 'viQbtJ9Q80k', 'vjRHryosi3U',
                'vmi3qdemEdk', 'vnM8W78zy9Q', 'vyQhsL4lcO0', 'w5ewrA2JmMY', 'wAc7ObR6D5Q', 'wB4ZhqE_lHM',
                'wHScc3DiE20', 'wP_919QfjDk', 'wQEKYioOiIM', 'wT0HzUOOEcY', 'wUnJ-NhdzWU', 'wXNS_VKPCBs',
                'wZIfU_J45Fc', 'w_wiJsX8TQI', 'wdi9NW3KW8A', 'wgvJDV516wg', 'wiK5i2QzQ_I', 'wlBgYrHx4ds',
                'wlEE7KQMKQg', 'wu4tOVRe3-k', 'wueWPyHw_0Q', 'wx-tm97Dt-8', 'wxF4edECVF8', 'x2SUH3dV3mg',
                'x2oD_eXLFdk', 'x49Cl5BA1h8', 'x5-csZ7mjNA', 'x6KCV1qrx08', 'xA2F5xe6Rds', 'xIsOAm7et-4',
                'xNH1J9ZTOl0', 'xS3OLwW7mKk', 'xUdX8XV50FM', 'xbYEC1XK9zY', 'xcrlU-lQjcY', 'xeQKldYDPjY',
                'xeRd3_6IRN8', 'xh-IdR5xHLM', 'xjlnosVHahw', 'xly8wGK_jcQ', 'xmgExCs2yS4', 'xnhO2nLvPHc',
                'xoYR_3ZlSFU', 'xqqGEZJtH40', 'xs5LLOI1_hY', 'xvCCT45KT-U', 'xxGyYv3oCi8', 'xxXNf-e0UBg',
                'xzXkeNSov6I', 'y76_VGcjETc', 'y9-uqBoYqBM', 'y99HW0gRpko', 'y9G9RTMGq5w', 'y9KwHiEpEmY',
                'yAVX6PdPLwQ', 'yCchRHG8i1s', 'yDvcJ-oUPnw', 'yEhR1d8njdw', 'yFDmbauwQYY', 'yIpC3f8uV3U',
                'yJDn7tdIcrM', 'yKDNNRf-VXA', 'yOWKtsb1hZQ', 'ySI9nOJuNDE', 'ySJsCDY-JaQ', 'yY6HG9za7w4',
                'y_GFJLp-Oyw', 'ybxPTzc-59M', 'yc493jnFhD8', 'ydHNhcwU_VI', 'ygqBORGO6gw', 'yjA5ZtOGv8k',
                'yjJ7RPHtPeQ', 'yn55IrAjGFI', 'yp8oZAVrGlU', 'ysKWwmZKzMw', 'yt7ufkgdJgw', 'yuJPkod16-4',
                'yxk4EbzxQG4', 'z13b3pi4FBM', 'z6KU1ZEYD40', 'z73Pyyzxf4c', 'zCf3WwpTZew', 'zFUZWNI7LsA',
                'zHIcNiTvj5o', 'zHYvmn5cpjA', 'zIqQgLSm-eU', 'zJxVj3o5Btc', 'zPAd-9au7tc', 'zRlPvD_4FoQ',
                'zVOwji6l3Pc', 'zaJtdGUsqlU', 'zc-B7qKNeW4', 'zlPwNQu5yhA', 'zt1d4O3Bp0U', 'zzCZTfw78Hw']

    # fil=["/m/02mfyn","/m/02mfyn","/m/04cvmfc","/m/03qc9zr","/m/07qw_06","/m/07pjjrj","/m/07pws3f","/m/0dgbq",
    #      "/m/01y3hg","/m/0c3f7m","/m/07sr1lc","/m/07s2xch","/m/039jq","/m/07qnq_y","/m/032s66","/m/014zdl"]
    # error=[]
    # j=0
    # for i in meta:
    #     j+=1
    #     print(str((j/len(meta))*100)+'%')
    #     if j>3:
    #         label=i[3:]
    #         print('line:'+str(j))
    #     # download_youtube('JultKcPcKjk','0.1.0','0.1.0','./data/eval/')
    #         if (list(set(fil).intersection(set(label)))):
    #             # start_minute=str(int(float(i[1])/60))
    #             # start_second = str(int(float(i[1]) % 60))
    #             # end_minute = str(int(float(i[2]) / 60))
    #             # end_second = str(int(float(i[2]) % 60))
    #             # download_youtube(i[0], '0.'+start_minute+'.'+start_second, '0.'+end_minute+'.'+end_second, './data/eval/')
    #             download_youtube(i[0], './data/unbalanced_train/')
    #             print(error)
    # print(error)
    error_list=['-BOEJc21cD0', '-EF1Wx_W5k4', '-F5paNmlgEI', '-NEW4CVyCXo', '-WndEqtjsvk', '-eSwEejvFqc', '-gb5uvwsRpI',
     '-hX9W86Ksvk', '00GZHSXnKhk', '03lZuPyQwCc', '05VYfTOuMq0', '0H7htxFpJh4', '0NkiuHNcBEs', '0dyfl-736FE',
     '0mwPjBQ1inw', '0snDoWbPrE0', '0xo_z8KR_pU', '1FPGv3Gq45A', '1FTIWvkJx1I', '1ZxLZG0gYXU', '1hpkOS9z3f4',
     '1lJXqptoQik', '1oxZj5KH7RM', '25Comaspgrc', '2GNSiLWVgyk', '2LskPqwPsvs', '2MHFg67EOWs', '2NZJIgd8zy4',
     '2PE5LzmyNhk', '2VXanLrOxsE', '2VhWd0InWyI', '2dYget65VQE', '2klikTomtMw', '2mDtvJCnIDU', '2nLPkozoJoQ',
     '34B5n63bnDc', '34qgZG-4H34', '3DhhUOkKoY0', '3TuLGvXm85g', '3uk0Z0ET7Ow', '47WfQjziZUg', '4FJDhRxW_nc',
     '4ql7qb0uL14', '56KXu_uvvG8', '57ommbIaofQ', '5AutSwQw3VQ', '5G1ScDu7glo', '5YK3WTR_O0s', '5cVwzQZqgGU',
     '5kKAWy5NkOc', '5sXeudXZJPw', '672-TXEecTI', '69k_Nljn7Ks', '6M45wCmePP4', '6OfUEP8EFRM', '6c-9TWOE8mQ',
     '7H8SEbiHC5s', '7QxcykJSayc', '7RFHhAEb2Kk', '7VnqKF5Mhtg', '7eZVRMEPI1k', '7vgdo_d23XI', '7vzasj62sUE',
     '81DxjcSmeRo', '86ZOEyRCxwQ', '89WZKIjpqYc', '8Gm6JPyHNe8', '8HH9q4ogr7M', '8PR96huLxpE', '8Q9URfjpCcs',
     '8WF4WNRwIp0', '8qh4C-Tb75Q', '8qi4Kd67Ft4', '8qsjlzvgaZM', '91LGQOllea0', '98qtHYyHxz0', '9CJH-JdH4Vg',
     '9F6RsvNM0qc', '9RTmwbSX4t0', '9jS9SPR07Fk', '9oQy4X7oqjQ', '9sER6dZGl0I', '9zN50tiq2cU', '9zWZAdcHYTA',
     'A4Jq0eN9fSg', 'A9DAEP1e4po', 'AMGVoJJfWL4', 'AOkOMWXRdzM', 'AS-lu9HCu60', 'AeBKGoECU9E', 'AfigIBp0mLU',
     'AjCji96erAc', 'B4_ruAnPGFc', 'B8jduAA_GyY', 'BKPbQ2GWJZ0', 'BWyGs_EeEXs', 'B_JhDsbO3go', 'BhG25e3s_F8',
     'C1orXgmSwQ8', 'CDClgRElouk', 'CKaM6h11rJg', 'CVE_qMz6To8', 'CZRqJ_QxFt4', 'CtgkXz89HYE', 'D0Q_8WBkHPk',
     'D60kWZC4wcw', 'D7xjedYUX6g', 'DBMuhDBlqP0', 'DBu8o3Bk0S4', 'DHpIGMIub70', 'DHw7yJIKIOo', 'D_q4Y-rI5s4',
     'DrjZDn3EgAg', 'E8X7XZ_iVc4', 'ECwdc-7Z5IY', 'ELeyi3cY17g', 'EhxFeb0nHzI', 'EnXcm9_68sc', 'Esjaq1m8KQk',
     'EthFkuz8oG4', 'Ev_pYJvt3dY', 'Ex2ucfMwrmQ', 'F9CjKPrOkk8', 'FKX5ZnFvVbc', 'FVv3FAaApwg', 'FeCfebzrwpo',
     'FfncwUZVvjs', 'G5l34WF2FeU', 'GIunOeFrZh0', 'GoTbmRD-86Y', 'HI-2Ji_nDhk', 'HN44iil7vig', 'HPCvWIRYkYQ',
     'Hw_p5rCIUbY', 'IHplK2PQ0wg', 'IY-_OLE45tM', 'I_NNIyV408E', 'IdenFdkeASo', 'IltLBXPsoBQ', 'J6HlnT4I7bA',
     'J6IrtAkUhHI', 'JHIOh8nE0WQ', 'JIGVl0bSro8', 'JMdO23mNIlo', 'JS7l6HPdG7k', 'JVR-DZn22_0', 'JVwH5vhrMpM',
     'JoFetPhqQV0', 'JofxPryZr7Y', 'K-WUs96xY7w', 'K9r_Apudm9s', 'KCR3YK-Arzc', 'KDzawV6B1vU', 'KPKaOU85Dv0',
     'KUZxIFzEXwk', 'KYL1fiUMOlQ', 'KbRftt5myc8', 'KcLoytYGd-A', 'KjVJX52iCo4', 'KunhpKbZH_8', 'LE-E3DTf2qk',
     'LLam57BWQKM', 'LWEPj69H4bE', 'LXZmEHSWXmU', 'LZEnZ3I6NqU', 'LpKom6E4GV8', 'LpU_9DdKbnc', 'M1n5rVvaHUc',
     'M6AsaLvOOrg', 'M6Rs3duqnx4', 'MFCEDh0tpSw', 'MO_Bdw3YHJ8', 'MW4LBPrcHy4', 'MmewiFAFJ7A', 'N-QHJQQuH_4',
     'NGaMfAdCQ6Q', 'NIYltObQYAo', 'NMn-9tvzQZA', 'NbqmsXrPC9c', 'Nfs98kE20to', 'O7cxuQyHuEo', 'O9dsUFYp7d8',
     'O9vFQG_h7Sg', 'OiTicO257Dw', 'Oq1b-6KVP48', 'OtSBLRPDRzE', 'OuCio2hai3g', 'P1RHRE2ROTY', 'PCJV3dyemB4',
     'PeAxrFZXI54', 'Pk85sa9OSK0', 'PkiSb8SPXik', 'Pm-LKw7pZ5A', 'PwVY9mx7ADI', 'QUYOfVx1k-A', 'Q_LxwjWYYzA',
     'QcOeAej6b1g', 'QzhGox1Nac0', 'RBcoDi-MtHA', 'RIBa5WJgRBo', 'RIgggNO-aso', 'RMsqMhneVl4', 'RTa0GdJOi7I',
     'RTqVqVQInhQ', 'RkznSn57dGM', 'SjEdkriqG1Y', 'Sk2V83M0ZZ8', 'SqUYrh2tmRY', 'Sz9JGvcu1nc', 'TEZXYVJW0K8',
     'TGN3VMU-rds', 'TWiXOjN2XEc', 'TeGoW7croIM', 'ThNH-4bO20Y', 'U0I8skJ3CLg', 'UJmrgFh84tg', 'ULS5Snuq_8I',
     'UO4ZHFjfrQk', 'UZLcHhioJok', 'UkrcILbBaVA', 'VH-Rbc9VM-w', 'VJc1ovmqlv0', 'VV2GeER66qg', 'VpVQSzhSd14',
     'W58c7BXsEz4', 'WD8TVzDCD4o', 'WDDBngegDn4', 'WDfx209pyOc', 'WQWkk0Itza4', 'Wb5U7RKOT6w', 'WeRVhyGIg_w',
     'Wl1bOlfU9XI', 'WrHCDT--UKQ', 'WtiOjEyfR94', 'Wvw4S1V99QA', 'XQ3Bv5K5UCY', 'XXvjDrgTdE4', 'Xf-irFKB0Cc',
     'XishfHZT7Bo', 'XtGQhsKIldU', 'Y6lkU_RH3mo', 'YCvOvWQjUuw', 'YSWiCtX74ck', 'YVUVbvgk6yc', 'YtPLLfyzeFc',
     'YwCBXxDdBL4', 'Ywc4_D3sKHQ', 'YybdU5g76Uc', 'Z1BUMF_46N4', 'Z2mS-eY0g0Q', 'ZFBfhGN_Mj4', 'ZQFZLu-D3bE',
     'ZULVl-kzo60', '_-z5aoNwgFk', '_0iMtaBaxfw', '_GbpS9uVajI', '_NLWvZHkjH0', '_N_TCs2ehuo', '_XPPISqmXSE',
     '_gljd3FjRag', '_n-kUOZk0A8', '_sPsvB0PWEI', '_uOmCK2XeaM', '_zUxoKxirkU', 'a6hQFPi8De4', 'a9ajriudKt8',
     'aBDNbOssq1Q', 'aDdZN0bXDbM', 'aDy5KNcjNrI', 'aMlyQysMdXM', 'aTO9V8W9Bg4', 'aZsaM0PNRns', 'alVfhRuFeVE',
     'al_vPe40xc0', 'altXfgbNIBo', 'alydjYAu4s4', 'atm7KcXQueY', 'ax0pj17NwvI', 'b-XuYaFCHlk', 'b8Pk-F_GqPw',
     'b9Gx-dw9vBM', 'bKuK6nu3R6g', 'bUWowdixo9s', 'bUuM_QJeyDI', 'bbDMGICoMDg', 'bkiV2Rotkj8', 'bvGOYIXgDuE',
     'c1MWFFRJ-wo', 'c8uhOIsBdug', 'cA13fTLAdW4', 'cLwVV_f2IEM', 'cMfOecMPlGg', 'cRCiQnKRzEI', 'cUzVLZypM5Y',
     'cYkV7ILQRwc', 'cjC84wnuW44', 'cpedkrWoxY4', 'cuRjCW69fiI', 'cwRQHKgnUAI', 'd1GcUbFJtRA', 'd8QZMJVgxmY',
     'dIrpIm-imYY', 'dLdMryWLwj0', 'dkookunC_HY', 'dupAZBORHdc', 'dwrnbgJ2mAs', 'eCvXsTfjYT8', 'eHX7AP3RM1c',
     'e_7_kuFlYNE', 'ecrJob5YdNY', 'es37q_dG7Fo', 'ewsZekIt9T0', 'f-lsMvfBE6w', 'f60shKKRYIc', 'f9KdVHm57KU',
     'fPEoegZm7eU', 'fXCMPr5Zm4Q', 'fawUEf83LT8', 'fhuufkjI6FY', 'fpPYEIMwlW8', 'fwBvqPuzP1Y', 'g8hiCn2lPmQ',
     'gCMlVyxRPik', 'gGeFh2qzCDw', 'geuZX67LfNE', 'ghz6s0fWy3Q', 'gm6ZAFsztZU', 'gzB2yQfd2Js', 'h3XC4Cz4U38',
     'hChxVDbmG_M', 'hGnMaFEmR9M', 'hp4QpHrKTfg', 'hvbj8tW9Epo', 'hwPKWs6q5zw', 'iK0CCBkGokM', 'iaYdJQiZrhU',
     'ib-j_RhDwNE', 'is9E_PKRnS8', 'j7Hzru3CLrA', 'jP8MINTY2sA', 'jf9oTrasj98', 'k8B5avou07M', 'kGPbA9wowRk',
     'kPuOsK1a8Co', 'kRjnzI1uv00', 'kVSMjlcSsiY', 'l8bis7ntbc0', 'lM5nxAAYcYw', 'lgF9muEpZUQ', 'lnq-KpZSZTw',
     'm2yPxziZyN4', 'mKeLOPmevJ0', 'mW5Lu55f8oM', 'mYabjBQaFaY', 'mhFVPYPmNVY', 'mhwuZTe5jIo', 'n9MceWXzRQM',
     'nHrrpEPBJ7k', 'nKG5K7j5mlI', 'nZqaiDLQWD0', 'na0zJA_YevE', 'nqe7A4IQmXk', 'o0wO84MNVGA', 'oYKuNlcqCSk',
     'oveJDfNxcA8', 'p6lx1ozL-tM', 'pCBP6_uprCA', 'pSJxQlSNDAU', 'pk__9yJTu5w', 'pkab4C1Hvks', 'pvtauHBAvUE',
     'q43gH9B-CYI', 'q5FwsIkJCXU', 'q6BraeGmvxA', 'q7s2qM42CQ8', 'q8rtxK-WkCk', 'qD7yyQ7a7W4', 'qJT4cbLVFuw',
     'qMcDbKF5Hjw', 'qWxvvNXnfFU', 'qbpljVsqw9Q', 'qd6KQfWMcd0', 'qoi38xLdVVw', 'qygzCLUnqlM', 'rNA9obsPFJk',
     're37z5rMIsY', 'rmX7XBEohvY', 'rpnrfsGwwUk', 'rzQdg4wRmxY', 's-_CH7hCJfc', 'sArGQfiV2Ro', 'sCge-CzawLc',
     's_U-3ukF_fg', 'sar__TZJPII', 'sxhrG3uvQiU', 'szOPoim44rA', 't385F1Xp_-4', 't6rniZNuoM4', 'tGw-y6n4ECc',
     'tJG9KwyBWM4', 'tX7xi3XV4Fw', 'tXX2m3qu5Zk', 'thQ3PeqyArg', 'u8JmK2TmnEQ', 'uInW3Rb5WsA', 'uW0LRcK_iSU',
     'unADFFVmEFo', 'unMlXpbpAR0', 'unjhSQnuExc', 'utrlD8tJT9k', 'uywF1JafL-k', 'v7b8eL96wAg', 'vB1KBizUCoI',
     'vCEBz9QIY1o', 'vILK2Sz4mX8', 'vJEuGVIefu0', 'vMD8HeOqsqU', 'vmi3qdemEdk', 'vyQhsL4lcO0', 'wHScc3DiE20',
     'wT0HzUOOEcY', 'wXNS_VKPCBs', 'wxF4edECVF8', 'x2SUH3dV3mg', 'x6KCV1qrx08', 'xA2F5xe6Rds', 'xIsOAm7et-4',
     'xeRd3_6IRN8', 'xly8wGK_jcQ', 'xnhO2nLvPHc', 'xs5LLOI1_hY', 'xxXNf-e0UBg', 'y9-uqBoYqBM', 'y9KwHiEpEmY',
     'yDvcJ-oUPnw', 'yOWKtsb1hZQ', 'yY6HG9za7w4', 'yp8oZAVrGlU', 'yuJPkod16-4', 'zHIcNiTvj5o', 'zIqQgLSm-eU',
     'zJxVj3o5Btc', 'zt1d4O3Bp0U']

    error_list=['-BOEJc21cD0', '-EF1Wx_W5k4', '-WndEqtjsvk', '-eSwEejvFqc', '-hX9W86Ksvk', '00GZHSXnKhk', '05VYfTOuMq0',
     '0NkiuHNcBEs', '0dyfl-736FE', '0mwPjBQ1inw', '0snDoWbPrE0', '0xo_z8KR_pU', '1FPGv3Gq45A', '1FTIWvkJx1I',
     '1ZxLZG0gYXU', '1hpkOS9z3f4', '1lJXqptoQik', '1oxZj5KH7RM', '25Comaspgrc', '2GNSiLWVgyk', '2LskPqwPsvs',
     '2MHFg67EOWs', '2NZJIgd8zy4', '2PE5LzmyNhk', '2VXanLrOxsE', '2VhWd0InWyI', '2dYget65VQE', '2klikTomtMw',
     '2nLPkozoJoQ', '34B5n63bnDc', '34qgZG-4H34', '3DhhUOkKoY0', '3TuLGvXm85g', '3uk0Z0ET7Ow', '47WfQjziZUg',
     '4FJDhRxW_nc', '4ql7qb0uL14', '56KXu_uvvG8', '57ommbIaofQ', '5AutSwQw3VQ', '5G1ScDu7glo', '5YK3WTR_O0s',
     '5cVwzQZqgGU', '5kKAWy5NkOc', '5sXeudXZJPw', '672-TXEecTI', '69k_Nljn7Ks', '6M45wCmePP4', '6OfUEP8EFRM',
     '6c-9TWOE8mQ', '7QxcykJSayc', '7eZVRMEPI1k', '86ZOEyRCxwQ', '8Q9URfjpCcs', '8WF4WNRwIp0', '8qh4C-Tb75Q',
     '8qi4Kd67Ft4', '98qtHYyHxz0', '9CJH-JdH4Vg', '9jS9SPR07Fk', '9oQy4X7oqjQ', '9sER6dZGl0I', '9zN50tiq2cU',
     '9zWZAdcHYTA', 'A4Jq0eN9fSg', 'A9DAEP1e4po', 'AMGVoJJfWL4', 'AOkOMWXRdzM', 'AeBKGoECU9E', 'AfigIBp0mLU',
     'AjCji96erAc', 'B4_ruAnPGFc', 'B8jduAA_GyY', 'BKPbQ2GWJZ0', 'B_JhDsbO3go', 'BhG25e3s_F8', 'C1orXgmSwQ8',
     'CDClgRElouk', 'CVE_qMz6To8', 'CZRqJ_QxFt4', 'CtgkXz89HYE', 'D0Q_8WBkHPk', 'D60kWZC4wcw', 'D7xjedYUX6g',
     'DBMuhDBlqP0', 'DHpIGMIub70', 'DHw7yJIKIOo', 'D_q4Y-rI5s4', 'DrjZDn3EgAg', 'ECwdc-7Z5IY', 'ELeyi3cY17g',
     'EhxFeb0nHzI', 'EnXcm9_68sc', 'Esjaq1m8KQk', 'EthFkuz8oG4', 'Ev_pYJvt3dY', 'F9CjKPrOkk8', 'FKX5ZnFvVbc',
     'FVv3FAaApwg', 'FeCfebzrwpo', 'FfncwUZVvjs', 'G5l34WF2FeU', 'GIunOeFrZh0', 'GoTbmRD-86Y', 'HI-2Ji_nDhk',
     'HN44iil7vig', 'HPCvWIRYkYQ', 'Hw_p5rCIUbY', 'IHplK2PQ0wg', 'IY-_OLE45tM', 'I_NNIyV408E', 'IdenFdkeASo',
     'IltLBXPsoBQ', 'J6HlnT4I7bA', 'J6IrtAkUhHI', 'JHIOh8nE0WQ', 'JIGVl0bSro8', 'JMdO23mNIlo', 'JS7l6HPdG7k',
     'JVwH5vhrMpM', 'JoFetPhqQV0', 'JofxPryZr7Y', 'K-WUs96xY7w', 'K9r_Apudm9s', 'KCR3YK-Arzc', 'KDzawV6B1vU',
     'KPKaOU85Dv0', 'KUZxIFzEXwk', 'KjVJX52iCo4', 'KunhpKbZH_8', 'LE-E3DTf2qk', 'LLam57BWQKM', 'LXZmEHSWXmU',
     'LZEnZ3I6NqU', 'LpKom6E4GV8', 'LpU_9DdKbnc', 'M1n5rVvaHUc', 'M6AsaLvOOrg', 'M6Rs3duqnx4', 'MO_Bdw3YHJ8',
     'MW4LBPrcHy4', 'MmewiFAFJ7A', 'N-QHJQQuH_4', 'NGaMfAdCQ6Q', 'NbqmsXrPC9c', 'O7cxuQyHuEo', 'O9dsUFYp7d8',
     'O9vFQG_h7Sg', 'OiTicO257Dw', 'Oq1b-6KVP48', 'OtSBLRPDRzE', 'OuCio2hai3g', 'P1RHRE2ROTY', 'PCJV3dyemB4',
     'PeAxrFZXI54', 'Pk85sa9OSK0', 'PkiSb8SPXik', 'Pm-LKw7pZ5A', 'PwVY9mx7ADI', 'Q_LxwjWYYzA', 'QcOeAej6b1g',
     'QzhGox1Nac0', 'RBcoDi-MtHA', 'RIBa5WJgRBo', 'RIgggNO-aso', 'RMsqMhneVl4', 'RTa0GdJOi7I', 'RTqVqVQInhQ',
     'RkznSn57dGM', 'SjEdkriqG1Y', 'Sk2V83M0ZZ8', 'SqUYrh2tmRY', 'Sz9JGvcu1nc', 'TEZXYVJW0K8', 'TGN3VMU-rds',
     'TWiXOjN2XEc', 'TeGoW7croIM', 'ThNH-4bO20Y', 'U0I8skJ3CLg', 'UJmrgFh84tg', 'ULS5Snuq_8I', 'UO4ZHFjfrQk',
     'UkrcILbBaVA', 'VH-Rbc9VM-w', 'VJc1ovmqlv0', 'W58c7BXsEz4', 'WD8TVzDCD4o', 'WDDBngegDn4', 'WDfx209pyOc',
     'WQWkk0Itza4', 'Wb5U7RKOT6w', 'WeRVhyGIg_w', 'Wl1bOlfU9XI', 'WrHCDT--UKQ', 'WtiOjEyfR94', 'Wvw4S1V99QA',
     'XQ3Bv5K5UCY', 'XXvjDrgTdE4', 'XishfHZT7Bo', 'XtGQhsKIldU', 'YVUVbvgk6yc', 'YtPLLfyzeFc', 'YwCBXxDdBL4',
     'Ywc4_D3sKHQ', 'Z1BUMF_46N4', 'ZQFZLu-D3bE', 'ZULVl-kzo60', '_-z5aoNwgFk', '_0iMtaBaxfw', '_GbpS9uVajI',
     '_NLWvZHkjH0', '_N_TCs2ehuo', '_XPPISqmXSE', '_gljd3FjRag', '_n-kUOZk0A8', '_sPsvB0PWEI', '_zUxoKxirkU',
     'a9ajriudKt8', 'aBDNbOssq1Q', 'aDdZN0bXDbM', 'aDy5KNcjNrI', 'aMlyQysMdXM', 'aTO9V8W9Bg4', 'alVfhRuFeVE',
     'al_vPe40xc0', 'altXfgbNIBo', 'alydjYAu4s4', 'atm7KcXQueY', 'ax0pj17NwvI', 'b-XuYaFCHlk', 'b9Gx-dw9vBM',
     'bKuK6nu3R6g', 'bbDMGICoMDg', 'bkiV2Rotkj8', 'c1MWFFRJ-wo', 'c8uhOIsBdug', 'cA13fTLAdW4', 'cLwVV_f2IEM',
     'cMfOecMPlGg', 'cRCiQnKRzEI', 'cjC84wnuW44', 'cpedkrWoxY4', 'cuRjCW69fiI', 'cwRQHKgnUAI', 'd1GcUbFJtRA',
     'd8QZMJVgxmY', 'dIrpIm-imYY', 'dkookunC_HY', 'dupAZBORHdc', 'dwrnbgJ2mAs', 'eCvXsTfjYT8', 'eHX7AP3RM1c',
     'e_7_kuFlYNE', 'ecrJob5YdNY', 'es37q_dG7Fo', 'ewsZekIt9T0', 'f-lsMvfBE6w', 'f60shKKRYIc', 'fPEoegZm7eU',
     'fXCMPr5Zm4Q', 'fawUEf83LT8', 'fhuufkjI6FY', 'fpPYEIMwlW8', 'fwBvqPuzP1Y', 'g8hiCn2lPmQ', 'gCMlVyxRPik',
     'gGeFh2qzCDw', 'geuZX67LfNE', 'ghz6s0fWy3Q', 'gm6ZAFsztZU', 'gzB2yQfd2Js', 'h3XC4Cz4U38', 'hChxVDbmG_M',
     'hGnMaFEmR9M', 'hp4QpHrKTfg', 'hvbj8tW9Epo', 'hwPKWs6q5zw', 'iK0CCBkGokM', 'iaYdJQiZrhU', 'ib-j_RhDwNE',
     'is9E_PKRnS8', 'j7Hzru3CLrA', 'jf9oTrasj98', 'k8B5avou07M', 'kPuOsK1a8Co', 'kRjnzI1uv00', 'kVSMjlcSsiY',
     'lM5nxAAYcYw', 'lgF9muEpZUQ', 'lnq-KpZSZTw', 'm2yPxziZyN4', 'mW5Lu55f8oM', 'mYabjBQaFaY', 'mhFVPYPmNVY',
     'nHrrpEPBJ7k', 'nKG5K7j5mlI', 'nZqaiDLQWD0', 'nqe7A4IQmXk', 'o0wO84MNVGA', 'oYKuNlcqCSk', 'oveJDfNxcA8',
     'pCBP6_uprCA', 'pSJxQlSNDAU', 'pk__9yJTu5w', 'pkab4C1Hvks', 'pvtauHBAvUE', 'q5FwsIkJCXU', 'q7s2qM42CQ8',
     'qD7yyQ7a7W4', 'qJT4cbLVFuw', 'qMcDbKF5Hjw', 'qWxvvNXnfFU', 'qbpljVsqw9Q', 'qd6KQfWMcd0', 'qoi38xLdVVw',
     'qygzCLUnqlM', 'rNA9obsPFJk', 'rmX7XBEohvY', 'rpnrfsGwwUk', 'rzQdg4wRmxY', 's-_CH7hCJfc', 'sArGQfiV2Ro',
     'sCge-CzawLc', 's_U-3ukF_fg', 'sar__TZJPII', 'szOPoim44rA', 't385F1Xp_-4', 't6rniZNuoM4', 'tGw-y6n4ECc',
     'tJG9KwyBWM4', 'tX7xi3XV4Fw', 'tXX2m3qu5Zk', 'u8JmK2TmnEQ', 'uInW3Rb5WsA', 'uW0LRcK_iSU', 'unADFFVmEFo',
     'unjhSQnuExc', 'utrlD8tJT9k', 'v7b8eL96wAg', 'vCEBz9QIY1o', 'vILK2Sz4mX8', 'vJEuGVIefu0', 'vmi3qdemEdk',
     'vyQhsL4lcO0', 'wHScc3DiE20', 'wxF4edECVF8', 'x2SUH3dV3mg', 'xA2F5xe6Rds', 'xIsOAm7et-4', 'xeRd3_6IRN8',
     'xly8wGK_jcQ', 'xnhO2nLvPHc', 'xs5LLOI1_hY', 'xxXNf-e0UBg', 'y9-uqBoYqBM', 'y9KwHiEpEmY', 'yY6HG9za7w4',
     'yuJPkod16-4', 'zJxVj3o5Btc', 'zt1d4O3Bp0U']

    error_list=['-BOEJc21cD0', '-EF1Wx_W5k4', '-WndEqtjsvk', '-eSwEejvFqc', '-hX9W86Ksvk', '00GZHSXnKhk', '05VYfTOuMq0',
     '0NkiuHNcBEs', '0dyfl-736FE', '0mwPjBQ1inw', '0snDoWbPrE0', '1FPGv3Gq45A', '1FTIWvkJx1I', '1ZxLZG0gYXU',
     '1hpkOS9z3f4', '1lJXqptoQik', '1oxZj5KH7RM', '25Comaspgrc', '2GNSiLWVgyk', '2LskPqwPsvs', '2MHFg67EOWs',
     '2NZJIgd8zy4', '2PE5LzmyNhk', '2VXanLrOxsE', '2VhWd0InWyI', '2dYget65VQE', '2klikTomtMw', '2nLPkozoJoQ',
     '34B5n63bnDc', '34qgZG-4H34', '3DhhUOkKoY0', '3TuLGvXm85g', '3uk0Z0ET7Ow', '47WfQjziZUg', '4FJDhRxW_nc',
     '4ql7qb0uL14', '56KXu_uvvG8', '57ommbIaofQ', '5AutSwQw3VQ', '5G1ScDu7glo', '5YK3WTR_O0s', '5cVwzQZqgGU',
     '5kKAWy5NkOc', '5sXeudXZJPw', '672-TXEecTI', '69k_Nljn7Ks', '6M45wCmePP4', '6OfUEP8EFRM', '6c-9TWOE8mQ',
     '7QxcykJSayc', '7eZVRMEPI1k', '86ZOEyRCxwQ', '8Q9URfjpCcs', '8WF4WNRwIp0', '8qh4C-Tb75Q', '8qi4Kd67Ft4',
     '98qtHYyHxz0', '9CJH-JdH4Vg', '9jS9SPR07Fk', '9oQy4X7oqjQ', '9sER6dZGl0I', '9zN50tiq2cU', '9zWZAdcHYTA',
     'A4Jq0eN9fSg', 'A9DAEP1e4po', 'AMGVoJJfWL4', 'AOkOMWXRdzM', 'AeBKGoECU9E', 'AfigIBp0mLU', 'AjCji96erAc',
     'B4_ruAnPGFc', 'B8jduAA_GyY', 'BKPbQ2GWJZ0', 'B_JhDsbO3go', 'BhG25e3s_F8', 'C1orXgmSwQ8', 'CDClgRElouk',
     'CVE_qMz6To8', 'CZRqJ_QxFt4', 'CtgkXz89HYE', 'D0Q_8WBkHPk', 'D60kWZC4wcw', 'D7xjedYUX6g', 'DBMuhDBlqP0',
     'DHpIGMIub70', 'DHw7yJIKIOo', 'D_q4Y-rI5s4', 'DrjZDn3EgAg', 'ECwdc-7Z5IY', 'ELeyi3cY17g', 'EhxFeb0nHzI',
     'EnXcm9_68sc', 'Esjaq1m8KQk', 'EthFkuz8oG4', 'Ev_pYJvt3dY', 'F9CjKPrOkk8', 'FKX5ZnFvVbc', 'FVv3FAaApwg',
     'FeCfebzrwpo', 'FfncwUZVvjs', 'G5l34WF2FeU', 'GIunOeFrZh0', 'GoTbmRD-86Y', 'HI-2Ji_nDhk', 'HN44iil7vig',
     'HPCvWIRYkYQ', 'Hw_p5rCIUbY', 'IHplK2PQ0wg', 'IY-_OLE45tM', 'I_NNIyV408E', 'IdenFdkeASo', 'IltLBXPsoBQ',
     'J6HlnT4I7bA', 'J6IrtAkUhHI', 'JHIOh8nE0WQ', 'JIGVl0bSro8', 'JMdO23mNIlo', 'JS7l6HPdG7k', 'JVwH5vhrMpM',
     'JoFetPhqQV0', 'JofxPryZr7Y', 'K-WUs96xY7w', 'K9r_Apudm9s', 'KCR3YK-Arzc', 'KDzawV6B1vU', 'KPKaOU85Dv0',
     'KUZxIFzEXwk', 'KjVJX52iCo4', 'KunhpKbZH_8', 'LE-E3DTf2qk', 'LLam57BWQKM', 'LXZmEHSWXmU', 'LZEnZ3I6NqU',
     'LpKom6E4GV8', 'LpU_9DdKbnc', 'M1n5rVvaHUc', 'M6AsaLvOOrg', 'M6Rs3duqnx4', 'MO_Bdw3YHJ8', 'MW4LBPrcHy4',
     'MmewiFAFJ7A', 'N-QHJQQuH_4', 'NGaMfAdCQ6Q', 'NbqmsXrPC9c', 'O7cxuQyHuEo', 'O9dsUFYp7d8', 'O9vFQG_h7Sg',
     'OiTicO257Dw', 'Oq1b-6KVP48', 'OtSBLRPDRzE', 'OuCio2hai3g', 'P1RHRE2ROTY', 'PCJV3dyemB4', 'PeAxrFZXI54',
     'Pk85sa9OSK0', 'PkiSb8SPXik', 'Pm-LKw7pZ5A', 'PwVY9mx7ADI', 'Q_LxwjWYYzA', 'QcOeAej6b1g', 'QzhGox1Nac0',
     'RBcoDi-MtHA', 'RIBa5WJgRBo', 'RIgggNO-aso', 'RMsqMhneVl4', 'RTa0GdJOi7I', 'RTqVqVQInhQ', 'RkznSn57dGM',
     'SjEdkriqG1Y', 'Sk2V83M0ZZ8', 'SqUYrh2tmRY', 'Sz9JGvcu1nc', 'TEZXYVJW0K8', 'TGN3VMU-rds', 'TWiXOjN2XEc',
     'TeGoW7croIM', 'U0I8skJ3CLg', 'UJmrgFh84tg', 'ULS5Snuq_8I', 'UO4ZHFjfrQk', 'UkrcILbBaVA', 'VH-Rbc9VM-w',
     'VJc1ovmqlv0', 'W58c7BXsEz4', 'WDDBngegDn4', 'WDfx209pyOc', 'WQWkk0Itza4', 'Wb5U7RKOT6w', 'WeRVhyGIg_w',
     'Wl1bOlfU9XI', 'WrHCDT--UKQ', 'WtiOjEyfR94', 'Wvw4S1V99QA', 'XQ3Bv5K5UCY', 'XXvjDrgTdE4', 'XishfHZT7Bo',
     'XtGQhsKIldU', 'YVUVbvgk6yc', 'YtPLLfyzeFc', 'YwCBXxDdBL4', 'Ywc4_D3sKHQ', 'Z1BUMF_46N4', 'ZQFZLu-D3bE',
     'ZULVl-kzo60', '_-z5aoNwgFk', '_0iMtaBaxfw', '_GbpS9uVajI', '_NLWvZHkjH0', '_N_TCs2ehuo', '_gljd3FjRag',
     '_n-kUOZk0A8', '_sPsvB0PWEI', '_zUxoKxirkU', 'a9ajriudKt8', 'aBDNbOssq1Q', 'aDdZN0bXDbM', 'aDy5KNcjNrI',
     'aMlyQysMdXM', 'aTO9V8W9Bg4', 'alVfhRuFeVE', 'al_vPe40xc0', 'altXfgbNIBo', 'alydjYAu4s4', 'atm7KcXQueY',
     'ax0pj17NwvI', 'b-XuYaFCHlk', 'b9Gx-dw9vBM', 'bKuK6nu3R6g', 'bbDMGICoMDg', 'bkiV2Rotkj8', 'c1MWFFRJ-wo',
     'c8uhOIsBdug', 'cA13fTLAdW4', 'cLwVV_f2IEM', 'cMfOecMPlGg', 'cRCiQnKRzEI', 'cjC84wnuW44', 'cpedkrWoxY4',
     'cuRjCW69fiI', 'cwRQHKgnUAI', 'd1GcUbFJtRA', 'd8QZMJVgxmY', 'dIrpIm-imYY', 'dkookunC_HY', 'dupAZBORHdc',
     'dwrnbgJ2mAs', 'eCvXsTfjYT8', 'eHX7AP3RM1c', 'e_7_kuFlYNE', 'ecrJob5YdNY', 'es37q_dG7Fo', 'ewsZekIt9T0',
     'f-lsMvfBE6w', 'f60shKKRYIc', 'fPEoegZm7eU', 'fXCMPr5Zm4Q', 'fawUEf83LT8', 'fhuufkjI6FY', 'fpPYEIMwlW8',
     'fwBvqPuzP1Y', 'g8hiCn2lPmQ', 'gCMlVyxRPik', 'gGeFh2qzCDw', 'geuZX67LfNE', 'ghz6s0fWy3Q', 'gm6ZAFsztZU',
     'gzB2yQfd2Js', 'h3XC4Cz4U38', 'hChxVDbmG_M', 'hGnMaFEmR9M', 'hp4QpHrKTfg', 'hvbj8tW9Epo', 'hwPKWs6q5zw',
     'iK0CCBkGokM', 'iaYdJQiZrhU', 'ib-j_RhDwNE', 'is9E_PKRnS8', 'j7Hzru3CLrA', 'jf9oTrasj98', 'k8B5avou07M',
     'kRjnzI1uv00', 'kVSMjlcSsiY', 'lM5nxAAYcYw', 'lgF9muEpZUQ', 'lnq-KpZSZTw', 'm2yPxziZyN4', 'mW5Lu55f8oM',
     'mYabjBQaFaY', 'mhFVPYPmNVY', 'nHrrpEPBJ7k', 'nKG5K7j5mlI', 'nZqaiDLQWD0', 'nqe7A4IQmXk', 'o0wO84MNVGA',
     'oYKuNlcqCSk', 'oveJDfNxcA8', 'pCBP6_uprCA', 'pSJxQlSNDAU', 'pk__9yJTu5w', 'pkab4C1Hvks', 'pvtauHBAvUE',
     'q5FwsIkJCXU', 'q7s2qM42CQ8', 'qD7yyQ7a7W4', 'qJT4cbLVFuw', 'qMcDbKF5Hjw', 'qWxvvNXnfFU', 'qbpljVsqw9Q',
     'qd6KQfWMcd0', 'qoi38xLdVVw', 'qygzCLUnqlM', 'rNA9obsPFJk', 'rmX7XBEohvY', 'rpnrfsGwwUk', 'rzQdg4wRmxY',
     's-_CH7hCJfc', 'sCge-CzawLc', 's_U-3ukF_fg', 'sar__TZJPII', 'szOPoim44rA', 't385F1Xp_-4', 't6rniZNuoM4',
     'tGw-y6n4ECc', 'tJG9KwyBWM4', 'tX7xi3XV4Fw', 'tXX2m3qu5Zk', 'u8JmK2TmnEQ', 'uInW3Rb5WsA', 'uW0LRcK_iSU',
     'unADFFVmEFo', 'unjhSQnuExc', 'utrlD8tJT9k', 'v7b8eL96wAg', 'vCEBz9QIY1o', 'vILK2Sz4mX8', 'vJEuGVIefu0',
     'vmi3qdemEdk', 'vyQhsL4lcO0', 'wHScc3DiE20', 'wxF4edECVF8', 'x2SUH3dV3mg', 'xA2F5xe6Rds', 'xIsOAm7et-4',
     'xeRd3_6IRN8', 'xly8wGK_jcQ', 'xnhO2nLvPHc', 'xs5LLOI1_hY', 'xxXNf-e0UBg', 'y9-uqBoYqBM', 'y9KwHiEpEmY',
     'yY6HG9za7w4', 'yuJPkod16-4', 'zJxVj3o5Btc', 'zt1d4O3Bp0U']
    # 354

    # print(len(error_list))
    # error=[]
    # j=0
    # for i in error_list:
    #     j += 1
    #     print(str((j / len(error_list)) * 100) + '%')
    #     download_youtube(i, './data/unbalanced_train-error/')
    #     print(error)
    # print(error)
    # print(len(error))

    # # process audio
    # meta_dict={}
    # for i in range(len(meta)):
    #     if i >3:
    #         meta_dict[meta[i][0]+'.wav']=[meta[i][1],meta[i][2]]
    # # print(meta_dict)
    # path="E:\AudioSet\Audio"
    # for root,dirs,files in os.walk(path+'\\unbalanced_train-error-full'):
    #     for name in files:
    #         print(os.path.join(root,name))
    #         get_second_part_wav(os.path.join(root,name), meta_dict[name][0],meta_dict[name][1], os.path.join(path+'\\unbalanced_train',name))

    # get_second_part_wav(path+'\eval-full\_22gJ5kB31k.wav',0,10,path+'\eval\_22gJ5kB31k.wav')
    # get_second_part_wav(path + '\eval-full\_gWEpDgPAho.wav', 100, 110, path + '\eval\_gWEpDgPAho.wav')



