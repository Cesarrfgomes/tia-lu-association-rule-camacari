import re
import pandas as pd
from collections import Counter

def preprocessar_produtos(descricao):
    if pd.isna(descricao) or descricao.strip() == '':
        return []

    produtos = [p.strip() for p in str(descricao).split(';')]
    produtos_limpos = []

    for produto in produtos:
        if not produto:
            continue

        produto_limpo = produto.upper()
        produto_limpo = re.sub(r'\s+', ' ', produto_limpo)
        produto_limpo = produto_limpo.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')

        produto_limpo = re.sub(r'\b(REF|GC|UNID|C UNID|C PARES|NO TAG|X CM|CUN|LX|\(\))\b', '', produto_limpo)
        produto_limpo = re.sub(r'\b(PP|P|M|G|GG|A|B|C)\b(?=\s|$)', '', produto_limpo)

        marcas = [
            'PIMPOLHO', 'LUZIANE', 'MICOL', 'ITALICO', 'MARANDS', 'HAOS', 'D\'VYSTEK', 'L&D',
            'DOM MATHEUS', 'SELFIE', 'MGRM', 'MAURICINHO', 'FLAPHY', 'KORTE REKORTE',
            'BILU BILU', 'DENGO', 'MINASREY', 'COKIT', 'NACLEFS', 'MONTANHA RUSSA',
            'INDRI KIDS', 'SERGIO MODAS', 'KYLY', 'KAMYLUS', 'ELIAN', 'NANAI', 'MAYARA',
            'BERLIM', 'OFF WHITE', 'NIKKO', 'CAT POA', 'VISUAL', 'HELO JEANS', 'MALLBECK',
            'FRAN FRAN', 'STYLO', 'LA NUT', 'SG KIDS', 'KIKARINHO', 'BERNA BABY', 'WAFFLE',
            'NATTY', 'ROTAS', 'DIFERENTE KIDS', 'SELENE', 'LAZINHO', 'AMSTER', 'TTHEUS',
            'APOLO', 'SFE', 'SURF', 'BRUMA', 'TREKKER', 'FASE', 'MIC MODA', 'MICOL BABY KIDS',
            'MICOL BABY', 'JULY KIDS', 'JUVENIL', 'INFANTIL', 'BABY KIDS', 'KIDS', 'MODA',
            'FASHION', 'INTIMA'
        ]

        for marca in marcas:
            produto_limpo = produto_limpo.replace(marca, ' ')

        produto_limpo = re.sub(r'\s+', ' ', produto_limpo).strip()

        palavras = produto_limpo.split()

        categoria_map = {
            'MEIA': ['MEIA'],
            'TOALHA': ['TOALHA'],
            'CONJUNTO': ['CONJ', 'CONJUNTO'],
            'SHORT': ['SHORT'],
            'BERMUDA': ['BERMUDA'],
            'CAMISA': ['CAMISA'],
            'CAMISETA': ['CAMISETA'],
            'CALCINHA': ['CALCINHA'],
            'CUECA': ['CUECA', 'CUECAS'],
            'PIJAMA': ['PIJAMA'],
            'BODY': ['BODY'],
            'VESTIDO': ['VESTIDO', 'VESTIDOS'],
            'BLUSA': ['BLUSA'],
            'REGATA': ['REGATA'],
            'SUTIÃ': ['SUTIA', 'SUTIÃ'],
            'LEGGING': ['LEGUE', 'LEGGING'],
            'MIJÃO': ['MIJAO', 'MIJÃO'],
            'MACACAO': ['MACACAO', 'MACACÃO'],
            'BABY DOLL': ['BABY', 'DOLL'],
            'TOP': ['TOP'],
            'BIQUINI': ['BIQUINI'],
            'SANDALIA': ['SANDALIA'],
            'JAQUETA': ['JAQUETA'],
            'CALÇA': ['CALCA', 'CALÇA'],
            'KIT MEIA': ['KIT'],
            'TAPA FRALDA': ['TAPA'],
            'FRALDA': ['FRALDA'],
            'PRENDEDOR': ['PRENDEDOR'],
            'FAIXA': ['FAIXA'],
            'MANTA': ['MANTA']
        }

        categoria_encontrada = None
        caracteristicas = []

        for palavra in palavras:
            palavra_upper = palavra.upper()
            for categoria, keywords in categoria_map.items():
                if palavra_upper in keywords:
                    categoria_encontrada = categoria
                    break
            if palavra_upper in ['LISA', 'ESTAMPADA', 'BORDADA', 'LISTRADA', 'LONGA', 'CURTA',
                                 'MANGA', 'POLO', 'BOXER', 'TRADICIONAL', 'SPORT', 'ALGODAO',
                                 'MOLETOM', 'TACTEL', 'LINHO', 'MALHA', 'ESTAMPA', 'BORDADO']:
                caracteristicas.append(palavra_upper)
            if categoria_encontrada:
                break

        if categoria_encontrada:
            if caracteristicas:
                produto_final = f"{categoria_encontrada} {' '.join(caracteristicas[:2])}"
            else:
                produto_final = categoria_encontrada
            produtos_limpos.append(produto_final.strip())
        elif palavras:
            produto_final = ' '.join([p for p in palavras[:3] if len(p) > 2]).strip()
            if produto_final and len(produto_final) > 3:
                produtos_limpos.append(produto_final)

    return produtos_limpos
