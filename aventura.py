from cryptography.fernet import Fernet

key = b'HtDYR59P0U2w0N8C6bc0omIj-PXHTljoK34NObXYRc4='

fernet = Fernet(key)

encriptats = [b'gAAAAABlRlruoGShG6n1s64PY1BZu_wsJnsIhYtqvVpBHV-4My0Smgtl3gc28ZKZwe-la3GJrRDEbScCeJ7Gl7G0pupzfjFT0nncWWwii7lxf5aeUQl25af5NThOhzhQDx6TJ57p__1f3SJJ6P2zRQe-GM6hvnAD6EfyBkJHCV5vnifDbAYCV25kVLkIFVLFJGI-bn9eianOV5mKtXzw6k936FnFNe3xweIgYoMBuGqZpRkR3D8Hzfw1_b-KJKyC1n6StR0inViN', b'gAAAAABlRl_BTotwoxyvHSBIZocdcqixC1K_5o_4h3yQTQ9qMOv_cjs9E8mihYVXzFxKscA8BzOzO3QI0GQowsL3QHxcK96fGgzBmc_p6cqnTHLt0EQ8Jz8xsfFDvvpV83AwUlVR-uUXrWqpHaZj_e4gh0MwmSx2RXXdI06hcCb4L9PKZujERPHjgMsppPItoclOW09zEboi1jex4Vti5THNZZnjDHtbGQ==', b'gAAAAABlRl_VIoZYdiY_IWHl5_UQ7nPMLTcXwS_xdxDVGhW6ZEfXXhoVsW0Z-pCxG-lacrgeoTyLBPBZ4Q3CxvNncYYVooHFTE5CTXKAh6cumVmfZxAwWLB8T-djvtcCqPxHFZXRCAE2eksUf0u1E3Ma6TfOP2FTn-Z9IWoxGbgRLGwI19Pml8lKGNCQqa47QOQBXTtIaS-xQLl-dwepR1e7Ks4l4rlwp_m-YmUvKkG6zriAS86AF1cYW5DAVeEgLstzF20f70sZMgy2rgHxgYQfqlSiCGpzn6pbS-LppP9GwlOyoIvEP82GZduoQyx48qYJ3wpc-qwSiLyuQ9vMP7KbPVOJJuA3H3JcXL8EcwsOyAQXCVx2YSX27wc10OB_s7Ci4P--IKNQ9AaNPJr2DUuh9-Wm0_9JcnfeWlG4qBU6KSDwEAGVWKgty71s60icRJF9kJhZiyQfGnRQM2onxPLyMYM09uG0iKwfwOf-_m_np-atXgsFV7uH98Z3XjRP0UPFRLXR4QB3jERo-t7RiCF2XrQpuCYAsJdTQGzG16h0Phae69sjY1PaBoDhKKIw5nBWEsk02bzTK4ZWqea1hVDg0J90-xWZqMNZ3S3z8tz64xoWA_PwkvIWMRgneLqs-2vJn-N_ogMBLG8shMXHXLk34FKmEYjHY1SJaz-VVpI7uBi1LBY53qcRFlvDv3joHE9lbuosslaXOlfq-SybWGQxRi1jXpL3B3cbNyoZWBMqDRbcsCRJE_Vqe-p73FcjWxsRCyGitqPYL2mx1NWcpEprPBh2nymrugctJ7dlKH0KPvq7D-FNJsE8xbxyWLpzCB5GR4-VkFfFe7hj7tejZX8J1-ayQO3cWxuHJeLoT_g2nyQtF7m_BVV4pME7Y3UIHkze6LGG37Y2Aaq48HLmseQf9Tie6g27Gm_mW9W_kXAPF2L89hug2QCuuaenCXdXt2PZOWfUqyKIEih87wt3TSHC37iCMEr8Nh34AULvlrW9NRHLYVBG6Mxc9bb5z_K0ndVQHIa0M3cfUMUANz4008JYvG4N4kWXM_YKHzYldwOZoyit9kYhmfZIuGuRzt_cprm6vlixltw7LZldtjNZkJ7m4x-D2PS8xboykGsDtJf342GK8QC8JnSFlXaj4ZXCiQ1t0cJ6qX3dUQak3l4VKDenLQq13dZENiGqzTjo1mroqQAWmRRJKep_44JdhYIsTM3t24IIWofBQbK3bkUx66Q244tn_Aw-6-zC7yiqUW87z0_BpbHgnnTsLJ3jAeXf4_HRB8CJUsZ8mKg73ue4IIcnb7L5MM6jgv86mTm_mha-_isq6e6f5aGCflffOYPGbkF-ZwxjjMrUs4uoxsD2iV4-4FBXKOYd3mKFkQ9-9bgw8VR85JOaOojqxnDMMR9w9IgAOIql3ADD-bKCowBB2AKyHrP8_tphBLAtSB0S1lrUpKLLwsdLQPPvE2AZRLTyDSATQwV50uprnvlVBWU6a3cYehHjbMTRwVSMfhdf8dPo5YCc39p0RvTURlSH0SqnBsPGC6tj-YdaFL5Lc9onLE1Zy2wFxHajPTiCvVYsg0pdE0ggt6uGgM_n34J8NfmluJKi7dqffKoeMbEzcQZ_HYwdoA8zOA5ca-eJdSjNpuuc7Brdyd1DTilxswITRWTd1XG5_7nP_SIH8qK5A_0A3t7-hFA1-CSGj-tlBHnNaCJWeIcwuMNfmviyAKqURSvscOxrDZcIKMAlf9pN1I-AtQW6JTYilGIBhC8155sobs6BmrR0IFsg9AZe0YX194wtgY9C6w6CMpi0x_bDb8IY1mpGgrUiIDgNXjROsyYi-zfdik-Gv61Wg3XY82GWM85q9y00pFrp83tliyzW3blqqUcJk0jnz1FKy9X_kdysrBM6_EGwdiygRV_fGFgQFG43-HdCXEFvniZ8Dv9BHccYH-7vg7iHFUmmZ4Mp8BiD9WIlKaqYj-nPyzUdqy5PTmO3cPwmdj0DuYCm0dDSnb4CaKygH9eR2MSR9Lnim3_1jxaBkxreHMOrDworq1MeS-aX5uBX3tb_9nkx0C6Op92elSp92E1ZqivGEsbgw8qI0oT5thJnLYxULtWG1XXVODajjhq9Edao-WxsrsiGuj3BNOQ7-bSZL8aI5CpZklIrLRlrcGtuGqUH32CFW0CyrQNahZ_---WObM0-F6zzdaKh5eo2I265aRbNmGMzUUYRWl_wJN0EmveXbIAHqLdJ3nT1h5U8-fTRTNVE82HCloVawKg1XzVASGsClzOChx2rJcKCfQOPdF4T1wB_Eain5a2OVZAaMK5oglfd88S93f0Ytg9lPLowbV_EtRr9RIRBYmVwJ8-9zHmuS_Fk6pJ0PYaMiUsiBHmaoIXGoau9ymuSqMQm48js2yFsL1hmdrKlQmBUMSmoThfU-XMgLediyGruWLxR4TVtnr-Y6S-4VFF7spY0IZzr0Scqhh77YededfowYy8Rio29_TgcWzMz50KcOfEXrZCLiOqoOYSvCJsGfnUAMovJC8X1oV3nCgsxODveV5BssZr3pJJ1TLxu7F-YiGZ0s0tSdt6u21lscBnqwTWBrL9TpbOFFDm7d2LKakA9fjKjE4wYm3BOQR5Lfs22iaAwrc8-ZW_wksMip4tCNkwp2l01ELjtl3uC_RqvwNv4CIoh0ues7nzheYvI7IsYIQBIUuQSb5NRQPfwu7QR9oeD0tdgj797OzFX2hRE5lt1xORWhNA7mZOfIkfW5ueD2evaG4wRxcTvnAen9XKciGtfsMET6gZ3wjQOgA15RCAEwdgQG9cguXmVfBLs1i6lwO5iz4n04W9fBzUc_bH6eb8cstt8tCj1Q4iqStBZPxnqivcQddL6MhcHZ__q_pNgvBAxgBPvvt8aFTrKPlr4BpuoosKqTMyffth4FMbrX0Q2SaXyRFvgy3jVIgJD3Jb4EW-yIR9qzfIXNZqfoOtWy5MMiPPlFu_X30g-qmw9TcmGRXMNOXOJf5RP5HtLOqg4zsjWz8S8obMhIH-TINduq0FVs7SsMD-OBXQbjfwlG570sbDVL36pm71HdMoGZYhHSOJKhpz4TpThFUUQMepvb_9NBy1FqQH3qCd4lMLGMzIuDKkPUoJFwLZxdlOvE9FXFugrbyIO12aYitxYJa_ACUPttZVwhPPIeNXhG1kaHCTOOVz1Lr0eOycFgfNT_o_9Ruxm9f2KI8V9A_JEd0S3ZocJoBaYExH9Teon9z99jIWZhpqiVaO5ABqCdtnTQFHhD8_uKhRzKthInaQ275tMSbbgUwkNVtadMH7IeZKKF6UHu8aJ8q1-cGETw-QzcMAp6ylxwPPfLWJ4JnXk2JSe5aBHbb-Ug-Lz61GFhf0h5jut6Vm0isIaOY5KfgCkebjNWXFfy-zomj-C_BMLEmuOfbS6_tpl6KWuD3h0s_pmMp3pOTV0e8gE6l6DBbhEstDpv9TRqzuFhg-NanHtftQWuL1lSDW_nEu7Hgr78Weqn2i7dhIbQhpXsYfrfv0feIiwfaj2mi5u4J2yG5dhWLpdqzHSBTjlsDu0hpTRObIk-h4zsaPdYs3cXtOmBnKWAVKiR7e_4-_lCgciNQg_2r0AV7dEZSZuKhMHhbwyq7V7A6elVppN6J9glT87dUjL1A5C4fK5RYRaxKaLGM4iwLYYV4sqWAOGxBMLMW8gjK1y4zlZQG60v_JgZrTaNvdrPoWwru7_ihkDwT94M5twQC3FM51JmfGZwhJOv60ls9vyCCzGdhZeJOgpeCIPx-4cvB5MwwM6JjKMLksBmXkRfwujHWeUeFiEmaJfaCwhna5nfop7b3rWHlHU49Ro-cqSnmuEZtOoqBdyKOgRxNiCgBkXCSYv3m8GxGzhmnwZsCRAsl2hiYurmQuT4YJqBBakQzEbzP7tTfIi1cyzPGpEVVYdIeU_5Sm0TJsPA9p5j4kz1wtuNhxgpqhiuiop_fgMrE3Se-phboXPUSAfNryNbapg5F8Px_5p1jKuMAHWwf5ozCgPCvPODFhl_1W_lLe_iWaY2yT-_ZGXAt0BqS7P1WMMlJagQiS_ebBQknKgLx557NSzZee0Sr3oCCO7b2a5j-pOHMtjCu-lJ0mnjdAZhhmMZaM3GO89mtrA7go_d8i9DTn5etJ4IV_yyTJKm4Nmo0cJAgg5vKHvupyZQxElMwmlqENaCmfStxPi3J8PMDbc_NIrkvo4Lc8qKC4Nou0oO2o30ejRbokWF_6Te3Sp-y87y1YtaeGqPUVLHe0x2JPZpH0kSzjnDhbz1snoxZzyu1tGc3t4SEnwE8bHlPmUBsgIqZoUEUgUw-O8E6dKEAdsGnubZ7sfhFxbluU3w5ewXWvEf2_9tH2GbYwD', b'gAAAAABlRl_u_EdgC5glisxjR3ouOPpmHPl8OYOKASaKYzPR2l0IbaNbuI_kfIFbc81nz8b3g8y5PY_epUg0vDsFz1lQds5oBjNj49FRUh7-qkeZ-SKu75y9qa0bmA2_rWzSwkIaaRceADdT8hYIyQI9kHEJhR2obsVt_uxBSShIz2zHAdH2I7yBZBxeBepI_2pWcKxi9L9QeDqw079WFajUF1FA3gsnJWoiZkyddDuNXkqwjyLfSgbRpClZWcdNvwRI3oCxvuXN4Q9EhU44oYURGyP_xFyGj46arR_PNNE9YXvBgDmR74PR0pJoT_oBtFbQ3K-JaLgng0c_w0ULn-MnUTZA9aHErxhcp1fvYfNrRNkS41DTuT6hGssZnnskWXbu3a2AYk2rhyeVd8UCBUbTrkyMw3zLtEVZzYlujy9B2rBqmHWfza-BPB7AWb3EJmKb2BAmtBOA3Owj-L3e0X9cgZRIKOW0CSpxaW0vIFgTGDbuKQp6-NQyCh83LclfO5hV1S6ZYJzB8FxHYNqwKAp_Rq5Oum9hcqeEvbUM1qlI3IxonKDwnzOzHeX1RQnFnFvAfo8scqnOT7Nb07V1HsrZiJnnNXQ3mHGOvdL3w6v6Yr1Mq0CfbwwSWhCoXPNC-n6nfZ6lFYU529FslMiEkiKFCC3VoiarkbBPnCcJ4ye9G5aKBigKkNCycjl5RikLxWdBJt-Bl0RSHUtoIhBMJxOrZJCGNqWcTFDFaBz_aleAyDHnLIZw2URwm6S5ET_a2EwtbmehzBPxkPf8tBDSi8CUuKE2917l95pBJqoLti0nzapmT63waTmRY0-IqLf3DO9PL-tFwTeWiLE-WZ9UusnPUpI8SSk-QBrFrBCi_sICmCiDpvQON6t2dEM5X3jr1OrjriNXFRVGIcOqr6CfzVem0-smn8IJL74kn_w6f1ZU3roPAekZJ6kg3T_EXhvtqhqV30vwHU2jJrykUmxQ9cGZEb7CHE7Z1oN3jOGVvarDoEleB2qQRfc92OdGz4R7SdFtxMJUNt4bshKDuZ25cylT4HBgykU6ZQtaoCBoz5Nx8guMIklJnFn30wW_gfP8GcpoYCvrhzbYPlROc4kZAS6meONX4FSAvbHWOr8YzJGH5yCpw-_SFHx8nmoieJ6ttr_pIiTuegVNKp9sbFNZhgdHFdzj8PMmE2reFDAp9Q8-qnLUw155_HDr6DeWKE20exerdgw66r1eLIlS7BFPg2wpn3cjmvXjOPP7Y6v8hWt4Jrv4bkl8qPt5FCzZx9tCMHgMw5upvTwOBRSZLQCvuPu9tLnA-r_qtf71OInVHuF42DSy8uksTdpJxuiUXbMTXzin7-k2zLTm8dRL1bG1ojn1jeI90ugx0W7ke_5EseMZlla8bBJgGyd70N-aidW7MPnC3_DiUDdqm6-jKBGq2KK1tlj2wyKwltLpi1RLvLY58VRj_lqTRnwmRcNWJ4qMdF-BgbMKUKQUG4Qhuh-1zeeWsSaSvHPBu0famFYmqhXSDW12zuJ8lMpYnNJoZ6yqg4q1X-snC-HWQ9Dzi-Qs8EjfXjWp1rLf2KhU-GPienJuUDFQzdl9AwNfM_xScgSC8Ox4TXDSUSU_Fa5Tn7ludQwpZY5pXEmBvMAMXdcSCnJbhiDC02DNEIcbB5fyN8HKISDvzVfthaUuSxHJSqmx2fSXG9rUqcS3yCUzBzMaxrA_y3n5Ob3TqbGhxuzGUGPJtAnNoVfK8Xy96FBGv2DUOYaaUeNCdRUu9swbsxtsiope7vA5nWgO33ScQ-zl7pM0TINO-27yh2jme1Rj7T0Um2Lhs0arbXMoBRb6iCtUwkV-RFpnj0KfAwAjP0bkfwSbT7enKlvAc68f75gHTNPF2TmW54nRcZqSGHSxeOIKbZQWdfQYv0ugz5tGHs73sZrJ1RtTO4WqX8ZtwLOwWcFkG_nR_iXJSTLxnCXLUTnVWhB8nXQxjTEZ8vL4gCYBIznKDKdziuutXzXBoSWQuAkIaiMpzYTyYaBlU4Hk2p4KarCYixdFhSiMJwg6NFCC5J6TcWzMbgP0mqUJBI837dfxcwvOUdimz_WXlw==', b'gAAAAABlRm3gbI91e7NQ-op4vz6MRBN1_BQrPbzq-NbqA0FGJnusikHLxWrvZ3DC6EcBJg9G9QEhaOxWmIWPe7HcLjaqS57fv2cLMoVg6Gbb3yr9zrFCP8iBdhaSRlgTKggfsDhb4W7-WLBNfevJV4z-IAbRTTBkqWyJRlnWj45CxCnaAZjil5d8A6KoioI0Udx-NZmt4mRBpM4xUf0taI5B3PwrXt82A_PQbtxNXKyQhDfROjNez3e4m4QwSOgvTammF_jvHb2mWbZjp4SqiCo_5n1DSul2fo_SedpFYCN58wn0uT_XJyoYf-aW25sbH_XPJ7mBNMsZmmNLdkSBpWSj9aQrAcEFF7kPwTLuzaUDB2nEOLZ8GYn7rFcCS3qCZg_v1qDsdmf6UsQzRXy_GYo0SCTkAlvUAYkEnPIgR_rJlUWJBAi1RD3urJ0CeddswDaNoAHRDkqSmeOm69Vhx80GMXNkKBeahzv0YotupK8mlfQOBSQZk5uij_UE9Ma9o87YDu4TIO0vA0jL_gxjuTnEkk3-i1N6Q7dxE9QeShNnnLhgc_Kd5rmToQc2JNS8OaM_ocVu4ieyP7tqaM-gl6L4tvyZ7E_zsvtblX4K_ALQevLkxfPOSuAP_XNV6kZ8WwuwtPHZ99zMpBGhluRZkChCiml12QgrNF5WLnuF5pXbU7_M38TpiRSzoMrhmqDz-XVrmJvYRNNE8QqeLN86ptZP2aDOG73V7vldDZSQWaPTwdLwKAL0dWm4PwBDVipvyaKaDkl2fERV6uakXZ-20zFhgC8M-UjxtJSARwBlu6LMzj8YiqqWQXRNfNRns5xtB3B23WxthXoEXWidUq4Cv-JhLmOlFjrHbzoL6H-8nXhZWfApojmR7j28yf_DvtlPh2NvsKCjP1PGIUOfMSCpHvJea_8TlX5eZQnb2iuo6ekAWI-erCUr3lcEGXC0AOhi1F3iSsqDXz4q4RZEM47ONYd4P57qIHjd7_uwK_-wqpYWX64Cjt9VTU_uR0nr0QBQkZPy5LXmcoUlN7QcDC2f5eWEirJ-04VK1TdRETUBCDY_9cPgYfMG18uVMDj816ywzAHoAQrtprfBjWjBMwFy0pVjZ6VP2UN2_eti0ndM35klMbPGrTfOJL-vd9qcThr2gxtrfeWEy4Nz7g5Z5Ph36Rtir7x-HXXBLKSbo4viG0IX_FmB36gpyGXKex3nliz5z-TcSFwSvgaSqoNeZse4YmMvsO19pl6QNAoLa6kwYCJ8i2id0JxZl_eR362TL41bqRCcWp1kUGOpKi8seGcHYdJeWLrN3MMzFEdyr8G1qBDz8b8GDks8z6dDgIasDLfPKD_nnhqg66Rr8MmtVTSdC2MBIyUp1z1Fyj8K1vlnSHOjiqEUEu8fwHcQlGVGNNZR_ajzYb2GJRNwuVBIxskY_7gvfKH0EObJuulXq9ghQScPqYRqfbKBAotjIwovQgm8MT6sFCFxrs6XvTnL9_M0porgsdSTrqRtwFwX34x92awaCxdiGZUQkDC8HTEqK0tnS_TYe0wnK5VPUYsJ_vEkGi4vLytkT2nyhpFxX4NvhW9MqcsGROzxlHvMbi3g2B5-WBwOnOpd-auVRHETklNOqdH6YZgsuuNp7JSrSeZ_qVr4kEAml_u8DHluF-uJjaPC5BGhS7rwn1kVeWJ2S_26d_387K_Kgy1ZOhwmMM-_p2_0Wx1QNTbbCecS749Kp9rzBjVs5qoSlMA7rQt2HVTC0-ZqW9Fj1BrwexbeTvjpKR_rsdiqrOropdJNISR9LChfwR7SPLoakj0DGLHh9-87mkyDLDH98QKKYO_kisiRWaDQdeB290a3EuRXGf5bQvlbxlmFkNpbyJxXd8RfrE76iYXpedfKyUVTXlvDD5Q4RS5YIvGht22CMwPDsK7oIm30YL4WC3Pxp_g1HJm1gHSgTdR9Gmjmy8m43w==', b'gAAAAABlSS_W3tx9t89-Jv9c6W89--lyrGOEsMpDnM_SOXzCwmo4mHRJ821vm60EY1v2Ys7kU9_IJjuj-ElhNS2JbLeJRGlCl1TM3dtKDgQxUdX2hl5Fkqg0LhQ0hlmJS-0on16kILC6XuBVQBVJGOvPyBmVoW5MmCfAiEoWbSMJQC_uH7KfQ48ElIkPUJDhMAqYuNV7WhKfwonAKf-dGc9zffLm9rW21xTORONnfHdmPVDJHMQF4T7F429O0hDj1jHbXtPjUNVq4b0diwschW4vVDKxV1RN1RCal9A8IuVmUdtSpSrVBqs=', b'gAAAAABlSTCFlxd0LkaTcJSsUa0DMoTva_K6bA4dqeDn_xULd4ENXrOO05VSVR8XcX_A36PFTkNtX8QSL-uLNhwu0pLRhm61z09XcjwwcKcVgtMQXYmuzMk=', b'gAAAAABlSTC4RGVHEpBIFxIuMi29S-t_ULj3VL5rzRTII5RLRXsidHCgctIUdqiIMtC9cSlKrkWAgOLFPPlZEqqr7bSXzeORAFuT111tU4-CViByFJX6zLwve59CnWzQ0vjlwPXHsdhXu95QvAj90pZbNFBkKjgnuZPIn4SucwmeDo47iy5ipj6JoLu4WI2P2jz5g-QjgagLnSdmNIriGr15zbwtiE0s66w3DzCMx5oT4zSl9fK0NhYTIDF-JeXj_na5FNSeS1aPAHnVKzv8ZCcz1cT9demch8VEbYgZFOmyAaf5F2HflgR0Np0dWV3wYl6h05QNqjMw18GCSeZ1cPWr1KIP6Ke3ijNK0mQbqmh2rw8K6qZLCRUYU4ae1VT0BQFuH8kx2tm1', b'gAAAAABlSTDvCr_Qj7d1CvBgNxGw8ZEmvzoghMDLIPvgMNyi-ycwMcmBI7VmFq87t7z8d0qbi2E5U0I-JFibRD2BGbyV2tGxiw==', b'gAAAAABlSTHWB3AXbHRuB9eeiqUsf0MEgrrenedPvzQjA6obZAocDn_n7pCcnP0hexYd5sc5i_HgcID_jT_VtVOcHeEa_qujIPKMWCjNtL98o4yrbhd0_64=', b'gAAAAABlSTIrpS36lVd-HNUyqSxTy0sXJis5qmL0wCPagiQF14rokt9jrcu6cSmxdqaLFpMqAejBys1rFSWP4-OqrbiBOXEL9dOofm8m_NjBaBrVAa_bl-L2hZ9CqR7PMZyH_Nd_d_wWcBfFSJMxgZuJ86S6KlvU1xg1_eR2W9rNtT-RuR9qdy1ZeBAlUC7SXTaYyeqdLsMU-kkDcu3w4EIZme2rXBGSpr7uduGkwQjbRn930n4CF6qI0F7OscWbRqjdLXngodWBLKGtDInPXsBn7TW4TvBa8YlYKIbjgSIjsmtqM7GxM-Y=', b'gAAAAABlSTJVxAK_N1zdBGAsTPPOYtxad0mlIiDSjks0xsClDdNm8bOv3Df2vvscnmBC5Ci41X46X2JvqSzfuMW5oq0EdbbLEXQ6rvWtnA2OaxkHGXbRNyvDKalaMIcmEMUKvNHyxxKdXX4cl6vJKt6h6iH9Hq5M6O30PMV2i0tsel8JclB5TKcA-J_B5ElkgfHCQomiVJnzvEUmrScQ3Ei3-1g_O_FcM7LjRFq74uL5z9tR9uqLoLkYW-NJV0k7b3RbfHe9ufOTv7t4o1tGBiiEx9sz_kmdZ58cz8Uk8GAkt8ogJASRV2gD2jYdLmcGsxv-zizJSte_uYk5iUNlWAMmTrpP24jwqCcdI9GQQVq6u6Bjmyw4V4zqAaW8t56VyhrnNkPjCOj_tfvauBEWm_aoloGrr6HNXuJBq8jgqOWuVIVOWemu2vWW_TPA8Hse1tC-e_gXfZAgzLvYcR3nyDbkrPtnTiDOEpg8N2ylWPHnZ4NGJUKuVNYH3mAQ9_KBflI0z2P2-3RTAzfKO5Ya2Cfd4DwgTsyhLXcV4bAmxTOBGcnj2Cxd8A4=', b'gAAAAABlSTKDkVPWMYFZ_8j_cCSq3RazSa1KALuNWf2u8rASJv3zmyJb1caQPjhrJweC23sIAAUuPSHGSvmBzpxvOtn5n40HCaLID78e_goo9sLEyK0VuxnxD8UiSoyqAhPYsbsKHrFB', b'gAAAAABlSTKsSt19HCDA3odVk7JHjNCijY8A4goUF0jSWhKUaPE5e-HDFhU1CbMeTEJZZTUfTxxfCTjhIRTdgq1fH-pBHyaId7HT3MSH2HS75x-D_mVpl_FxXr75yCtDTraBEXjfkZPaZ9Ls2hz2cPQBLCVHgNIDx9S0gz6zQ4xXXgczqYGgTx_flPVlurCsPtyLzvOqVpDTaw1Bm5k_QvpbciB3i8tLzHNWXhrmniBSFa2GySq2ljJnb-yxmB1gxSrroImW51FquMtfa_qbK-Neh7jUq3LIxRcntSow-1EjDuEoqPUhLNOIYn8fJ3PmEng5FUBLLMA4g1bTAD6d9JLb_hEboIAB01l9c7gTrKt-dcY_FoOcBlIIadpqT81H1GSvP9QVbGfczlvhyhQ9bCp7gAwhaNT56Qwdu6U2IKhYh_LpF5OIOYBeFhexlC2oU9Sk5XVoWasqLr_3tF4-3fcfrZH5luvvUbnEmH7hwus-AWbKpzra1RdL7V9hb1uePEm-gbKyf6QcWknBuU3W0l2-zjaEHxxxCYaa1qpV4q7wOMSc8QgrEFi-a1bnYNgNUsjZ_b6GcwwiXjBkUjz4C9v_e1VpTIjfcF9WJVeouDq4GPvbYKfEOi7Iy_zvcGJjzVm0AGTqwdvt', b'gAAAAABlSTLS0ufjT_tjunj2sWFe7t41KzoFMd60iJioBN3DeCBI3CnGo8gxPMFZTud7VSWsUKahz_Vcb_5dOrrFHvGBUSBNvYnZOltLrs9gz7kpmS8buWwt7qLi8yJVsCL_GMn5ms7s', b'gAAAAABlSTMGtg1KSxKCN1f5O00uHvLiIpnAiJpVE5oZ-UPG-AEIf-nCSYMYIT8PCZW2HXPaui-lciWxxFFt-Uclj5KcWJTQmyH8nCMnz5aBSIfBTLL7o5dwIZEj_mjPRGPpB-8qhWWf', b'gAAAAABlSTMjPTx-o608H9-Ckp8LewkUnDFKEEcXvK5bPan-I6rX8_t5cjWuRFagYeA16d1YwDL-X4CTGsTLLxZjueCygVof0YQO06GVhyPbLyTj6adqkVXM1EDWT-MBvTw8A2QBlU9eTeCJte5bWpn3Heg6fOrdzlnOrOCqoPWgcQ7ZqBjlJra8-_w36mmYMPtvRJ-wr6dY3PEjRAInrsZkeCge7q7Gmd5-CUOFgF-O8HISZSNxD7Cor9Zm2n2j0JGxxK-10ll_', b'gAAAAABlSTNzgastuxtN_WCo_w2DGQzhZmbE2bRp0Idf1nU1WKiNj5FVdH4SYx-aYkbLsjKjT5aZlZrdbsTeKOwpftOTJ_rtRkJEz_R6YdNQKdp1EkkHY3g=', b'gAAAAABlSTRFJWQNkj3SKW3eVC4x3_00b1x-xP2PiCNi59MWhxSQVBEr0D7LTrzwNrI6hderkhvEe9xIeUEJfHTbfNfz-V4F5u_mq0wXVYyERT0SDo7JKbg=', b'gAAAAABlSTRbSxsEmjj0v-gmMZRvGdjKZmHui2q_hcFEURdyA-5_QI4AXRy5PuvowkfS183LrGSRGTAyqBtocLqK8dOQOX9kPMm5GEACZ_G0UUjzW-9H5hGNeKTIIry16ubKV_cK-LcjAwYeQ3cawev1iXu8hBx5eKZid6bqzLz-iFYBuHh6Zss=', b'gAAAAABlSTRxhRNH22cTuEuQlpUleXowGvVXcNUKPrah3zW7GV_GA0TD7DqB178hC866SmFMvR3pwwGmlr0KO090KySkpZZNoUDuXyS0KsmjkpAghA1DprHZgwqun93d4P292vtxpx_L', b'gAAAAABlSTSPWDBjlv1935mgumCopyMRE6gmLOTcyJuLAOt3ghuc08GgC75x65b8wsTxLd1RekDaxTaHoxWgtbrb6SnsbS6j7JvZkyEhLe0rKqJFdlfzzOXtY7wYhu_sl397CKdyBLVEZ7FRSZVb2pXg107E-uju8Rqh5Io_zqSZ1LDFJgfzPwusf-CEnoTzIZBhmPTcc6XZ_ENnMnexcl_kEFfediKETYtReDHJnjIMuZX6C6J1v8sBY2ljZ59WZThMIjZENoi5HgWpuweFKUFNTsByu04NdxTLRyTgPI8b1-pIaRttBdPEHAKnwVXY79xM2T4MXPIQ1463re8xCVz_BhiMmTtVAEZZWLlPyZgjqdfIXCLvZ65dSGF9dkKgOKZv56FmRdcg', b'gAAAAABlSTSluqDfrB9ei_VX2j41hK5PaSdiqzl-kbFuflfdxwu4tKZo6J5jcKdB6b4FF0umRsIA0ba97fjXcHR9_wGmUUQRIskk_u39iXe1Sr4gGrVje4kowCfEHYWjQt5inmUHO7Db49qSe_JcHAHlONIjfVqmd1s29g-mUE6Ag19Bvend4d0FRmUSGWzZlFh0tA_se6eg6_G0LxCvOvg7bJarrgZXkCOItCKtl9iTMBqBb1CyGMux0oWjuhjYk5WTvMcq_QTb', b'gAAAAABlSTS4kUMRTqHpQnMfNiwHteTIihqyxazlwPsPNp8L1jdfN6ACQYz7c2j_iWryAFdr24-r9Wjlo3fJOx0BrtlvAwmFS-E06BEhRHrilx39Py7fSwS5P8gn8DUyr3f0HEFjtUmD', b'gAAAAABlSTTJ0C4GX52n9OszT9n1ROtifQqcee5B73rvUDSiOT90bPsUlB1qF0ZFZCFr-t8bDwO36F4dABVAyXUR9XtqTqJK1EKNghJBVUm-rSS3MwMtIec=', b'gAAAAABlSTTw_seMgKsCfBelNM1oRIkKJ1AxXpF-WvG6-9qmg5gUGgUhdRXg77PAVQsf_6XxiXW2O8x74-SanLtqxw1Rv8tpv3aGVyC2uyHnwkh9YGXT-9UXrqE0LLDn23hILsXzCb01_xmvV7uFR6XtolcLcNacTXfQt76gUGhXD-Bo0Asj64s=', b'gAAAAABlSTUQ3cOUb7aq3Hk4p4hG_PEXX2hjVs7syLs4z_IUC_s6g2AEQxfMgF1Cw_5dp6XLa_DGTNNdotzXAj5YQqwfgzf8v12UlV4dnIukfUzuXBtPpttymEVjFf5wChkBWvIo0w2X', b'gAAAAABlSTUqm8tVisrXCSmB0DEiC7QaAAwfHtiNQaKA-Vlthg-E3ijeNp0Te3uTAbZ9tRs3BIByAo6C3JKxrKvsra2AAw25hEH6au--1wbYo1urelP3MyT1xh8a_rozE4FqAc0ol2PB', b'gAAAAABlSTVCA8Fwxb4QHojN5wrHEOwKP1gZ9t7kmP0g80B1iwhRSGJrtAilMR9Miq15LwYJ3HPext1fkD9vF7CE6qJUukiMUQ4YAISnvGPVbLTL-cQdJOSDxg6MssJrj9Y27wrle-aYUFjfIUar9oRNv9pvThJFvA==', b'gAAAAABlSTVeG9tcGaWgloeXGDned3J8H9JKT7jbc-PykdJ_QSvmlvYlc4ksnbHXf408BhZClwEWaSfjSSdQP_EUIIx-jnzvr0xYjSL8g8crmmF2PIDtnkQZN6_4472ng28w6TuNaIuyzCDc4C88Kcn8jyrdN_kXqkQ4pud86Ipm_ICLeMFHKD_xr8-HEh8Qi2snexzKLHgI69dQXEeiR8hkeopDjkYCU5uolfjpgh9OUrZe-k4eO0mjbfYdv8EEx_w07WAZeIayOKhN-NbSbYq5NumOrQVwK3hgaMig5zA1SD7xolQmy-NfLGujbhJ541ryzow0n837UcxqsMO1yENSoS7Ny8sSZ_1Z3Z4WNUpMT-5CzK0SmQk9Ga4Xj_6rcfDJo_T1DQ02c0DRyQmE9umA73Mzhnorm402E9tYzFmBvUAJLD-rUTP2NOHs9tpB15UCI2At3AKbtrGjLA0h-TxpeTGeHCk95Q==', b'gAAAAABlSTepfjoBUrX74I1KK4FxhBn8CX7Cr1W4gmxF7QH8tbaRjma-tNMemwXXAhCx72oA5f9_EYxw5Hh6YFiLPL17n93M8gdCifdHNUN2I_GsEtrMDmLeyrxk4bDnYOdz89Xs5rK5', b'gAAAAABlSTfBP68S1yo7yb4yGoE9I38EG6qhE64TjjEDp0Shx5V-Igw1lV-ZwQNWYc24bQtsaoWDaIfiWOZal3COYtuSQ0R8HAuqE-rgLFi_CA0ysapKtEUrkk8QqxgXP3w85i1MK_jIDOF-S_nE9QqgknloHPa8BcWuOkMN9eYh8wSDtLHtj1ZJdzZuT_i9JXYVA6f9d26sJgRi_4L8LAcibtu_M0VL3nNX_yOz7hjIINk7P3WHFPo=', b'gAAAAABlSTfWpsHWE4s1vtpDwCwJqpILbfLzdaJRN2s2E2cxkeLBjagbDkvmGPz078R5hZVrLd01JZHJNr3sBluB6-pCFZNrAWccuADF1W3njUDUDuFkI8ePQuwKmobHmAIRSA7S4mg6diINRfIoTOEduQVE3diH8Uq8rwfU5RYJhJw1eOaFXG8=', b'gAAAAABlSTf0W598SBMU7_O3dTveyB0oVTb5GWozBwumKtghRd-KcQ2FFSZIOhtmkhsiDRMf5F9MK7l_h7mJml-StJyoq1V7Ku25C-lIUy8xgh8iOPfOV-0KLgr-G-bgPMls_ERhF438IsbBTj8Ij2RSvPC-mJF9REIXgqOr-pTkRS7u4RDHlAXgjEl3cGOZHag39WTnvssMhp-w_6icUyLIGaHaY_fk-5nEww1XGawyYafxFYIy145H6NSIiMiU0PlcscIN69ZX', b'gAAAAABlSTgPJgMHTq1cs7EkfOVSL78uCOeWPWU-KkAOxWImXaKnPHstte8qjPWN2Nc2ifoGchWF4R5tM6x2sNnoW5KOdRIZP6sv6hkBUS9cPP7sQZ5fOngBrgPmEKMQ0CE-ykYMJ7NqPUcWss96ypmebNLiEfO_dBQywesDCegdAvGPVIDDvp_gdBmaM6eOQ5duM2bFbYBqe-Lz9gbiOnRHIgUQdHdGVQWjmUrmmQ_NtjtGspXAm2U5pkbPCxdeBsf-krUo-7H7cDLtH2tRhBW2_Kcxw_PCz3XspBD6P3ikx81jzyTy_EHcD0LccNbIPsrStU_9fkFBtaiLrcyG-RSrIdZBUmZm7Z3O9LEgvJTR5VPmLhqYQZM=', b'gAAAAABlSTjGy31IzVofqytBKcJRtCPaIuvzLI8i8TNahH4I4-SmV40WGT12SBdnnrO_gHkjKifm1sLYYASf-lxb1B87C5BvmjY5qo68vUjYFeQBORg7hjZPlPgq5BzsbJ1-ex8gEDCFDX91UpAOEkXWQY0mfg-iGHd9ppf4tjAzkR7c2uNkKW5sZ_9HH9vXHtrBvEc4Gu1M', b'gAAAAABlSTj17B9PlHEeHYHSu_JFMcO0lMa7HsblCS0WLW59eQHdIC1bsgK5d7CB98cHDQRuRXKLjeQpVdIr827_VrKURj5TMyu7YeNrx6kkruI8DeW-OUbuoRCBnxky3gNVK0W3VVvIiivZjNhO-KZrThdl8MTZTkneSV-GD1OVE83n_kIgCO_Ccg_9ytIRPxdsGfY3rSJcHYcXa5T8dT_D-sU_YAZKnv5S9TgMiCQrLyK3hN25PIc=', b'gAAAAABlSTkMJ54jyO39mvS3ezWCELQGJuzAhnvgV8qz6VNaQwNoCa5WuGB-SMW3WswbF6BfTjlLk74W0ww-EQF9g2n-M6Jf-nYLvNzqQojWiFjeUrdV6FKLHDFVKdOrJEHkDHCzpB0W9BDoQPIlaf1lcInt2ZQZPY4wYcGgeMddZHoncUkLT5jGZTsLj_yUKAuj-j1vxecR6YCFHM-2dPiKMOi8W6uHsw==', b'gAAAAABlST6VLi7iZU5bs6ghMlZZQ4mDKYYbFVE_tDu85A1WeMmq902xNvHbnSCGb0UmuRo50pL1867zFrVBGdUvpyZC3SHvlcLPH3hLLwyXwjfaGShbunJg49J3QzoPFH7K9lQASrQS5e845fkvjPRTsextQ2cV0Q==', b'gAAAAABlST6vX-ZsH3fWoUg2a9QSVAezFB1OehB7tcxU9q6XDI8ewfrILNSFWNK0OUEWO_KdTeKTFJKLwnqFF3Kit83JkYFO6Qw9XgnfylDe4Umsw2HpC_HrdAG0GDjQ8HE3OR2t6DFo', b'gAAAAABlST7l0zul2R5hTfxom7IBRLjpzal4mL7YIf0Vyrq3ZGpwQk7H7dQaCmhYQxM20WgfnCtideEkDQbCASdtZKnR-y49BHCezeY7aEbax8dPy4ogKOYrS9uVmDKKTQKFjYf3wNBW', b'gAAAAABlST8a9d5Z5MxOsP9ExYiDecYlE8eJ1giNZZg_id51kqUgjJ6x0cx7QqWyAFu5zac2YXtCRx4HAfIQMHK95FivNyYzXDfbVrbVjR9gLtkeEJLwhOxqDhy_tNtMjAkW_0T1vv-8', b'gAAAAABlST85LYG0mrVsbmyPftcEhGoYkQyS4fXLVByvds9is2aRUNeRzgJRel9pZbwLuy4e0UxoFaZ8XaC325UHkk2y4T2Eh1Krw65ZHHzQvCyVXcS2Gj5qeGkCSY6xUZHDDAajxNVy4hgfKeyNFXUmwbowLYK93ZfbU3Wgwmmf-Pw-65cKc98=', b'gAAAAABlST9-FNhirIO3q2vI_zZd1SLxA-uXlviEQIlQqMW6okbauRdo7GuI-3h-lO-ihzaRARWMOv_3Gowz8yPGmQTqHVfPNQ==', b'gAAAAABlST-zm2H-8ctEeLhLItY_p2bwM3CZ9hkmNnLaXyTyyyOIP1niwc8rfQqNNr9TBNCkEhIr3uf0b82Y7J2-xO5ZGKlRvtQs05tn_iFswNxdfDc43bU=', b'gAAAAABlST-3PshExQX2XuHrWMWygHjFf_ipkNqOuDqYmpDKbe8jIM-U4z3M4b1OWSFJZw91tNTDq6EjlLYXrw5s2FZNkl34DA==', b'gAAAAABlST_OCZHK7SxrxwJf_YyJ1QWAJ1cUbmAH3H2LCSsf1xdGPceNlBHvfT1sLR2zJLXFO-6cmx74vk2TUdjHoA3F7wZDhA==', b'gAAAAABlST_jbLTEsaXmGoJM5Q4JepUhS_sbb24VGcH4uePdutTyEuWmBPek3iBqhPZfZunc_gTydO8keLK5s03wfgBIEOBLdg==', b'gAAAAABlSUAbg7N-AyVW1AgbsSHPM_x5e6ppHWKs0ngst_zvl2EFw5n7_TSroOJIvotk_xqi37PeHmW-xNsoDwg9KRJ0CqBr2A==', b'gAAAAABlSUAx1MDuSCoCEONTAlY1KPSAy8dVIz4m_RjGyzBIGS6ULJ7dKo6pl2IeryZ8PmXyfAyUxWIvQ8-i18UxJZfzcA4ngA==', b'gAAAAABlSUAyC3d-Gp1Snn465fYttxXffYny1NOW39yStNLmB7hxXekZfFuOrrEUrhExUWNcO2euSn-VgfhgItq6w8Agh6MJRg==', b'gAAAAABlSUAybdMIDQdAlUr1USsmvIA9wZdhwK_pVqd4NwNI9zmLws9u6-8649REtnIQmSyFVMGdd3bpdkcgnm89b_x-aRCGTw==', b'gAAAAABlSUECulGf_X-oxtmW_FMDRAg5GIzNV7-ZbCVsosthArjbQeRC1g_kOyD8YxrS5FWN53ki7lrF-LjWcOa7cWom7wq28g==', b'gAAAAABlSUEIWjkG4oA4SUP0Bdm6LkM6Puybz7ElTI07z8vw_AbgYPVirkRoBToAYgRRyYLpFHqsqbDz2Gk2HVDpQX3Ar7yhOw==', b'gAAAAABlSUEZUnTt09UkCPfiIiCLX7IUGMnpwUbE5TZor4XPaDimyfyQKvVzZ1y64-74_-78VobSZ3N7UuiC8KN-i3eiMh44bw==', b'gAAAAABlSUEpLnw6HnppPpUA_53AYnt8eVPHAKqHmsEfOcDyPSb6CK1oaYFkWePnVHXhXRi6I1w3hTpLYVf5PfekwdVF7hMW7Q==', b'gAAAAABlSUE1DcIfAXDmbwWXo_wxm5EHKZA22EbNJfzPWMq_8IPye_M-H72lWbcdYIoBykzlHMcwW5ifzi0VT1nGadlg8EcWKg==', b'gAAAAABlSUGCizOxjFEezkj4Kob_SkZbhAjr3ffXvBbJyE6wf5NNGLw-IN0OOxHpfeRUSbrZaI4A5ZY4StWU4HVgsJWbCspuXg==', b'gAAAAABlSUGpYem4Js483CPnNCxi966VSbSDcVvqGmqWddOS99RcubhX78HUzruOZ_OZcdjOl69HEIwXoXXaxjc-QwQNizwY9g==', b'gAAAAABlSUG8xP7nxwqJL8Mh0i2luMwnKkSrzuR2OgVoZ77eQI13x4CTVgPdtvyMzVzwouRL3Mbipv7WAIVlNwmkGhs8SjXv4wLGZY5RyhdP6hHzsy2SBUE=', b'gAAAAABlSUHxBix05wPzK6szwZ31GdTZ-mh8iCI8tjVy8eHRhAccospaieZPedOsp6v5QYzHoIUpHyZz8zRfuIq3H8l8TWYViGGF1m6RBdpRGiwZAc3u9VU=', b'gAAAAABlSUH8e-qvhJiCtXJ51Xhhr5lnbDy5KAl-P76-FawSNEMTRSKIsdnfDaa4j3lsxR06T-uE3_Y7hobixArJLB548uLPZRw8uDwD-6cNaRMUImHHAaU=', b'gAAAAABlSUIHeF0nWpgFWDePYx4KzfAbt8PoCoaXixGHEzpMBzKirsFCOgzH8GYlzODJyJ2GaPvykJr-HbmdRsIyiMMm_an7YmSGpHmnWrEk0Q_0RkGNzXE=', b'gAAAAABlSUIU7TcBREEP0jE2_f8v4TggaxAAlWPvOtljKn9FXktKdWBh7ItAPV9am4ZQTwEi3RGtRj0Gz8JuF3WGRZ7gA5-ejOqa3PGUE55nRQd0Lg72QRQ=', b'gAAAAABlSUIkP3YJTacH9F6nIjDPDdazN0VO1T2p9LVosaJxolHXeAD1uywUOFAlflwzeCwUvFT3wm9hkgU-4fb7u4xCriDmP6IjZRON9IofXzxLu_rj-tY=', b'gAAAAABlSUIt2LgFPUjW4nsChwyWEARZ19ZtKmJIvW3IsAJww3CYB1qJXxJVWdW2Roj40_Zplcivs5MlaYh0PrcWI_CbPfEia2bHwkt-5XRm5oVKf7rhCfs=', b'gAAAAABlSUKGCpUuMtMf7KTrFBR8LUvo6CZ44Wit6YXdEPl5INTFZc4RqJ9D7Ll2-R8wGMu74UGZ1hY0x1g_3pxWqNgLUPW8tE7X5pau4OU0B80JDozyl_591xOtor3RJk3GMj6a0xhM', b'gAAAAABlSULYHsU9UTi2S4seQ4LKvahoByvpB0H0cJYu-uOy13dcjf-rdFXz-M9XRIfDraYLFZjn2galaZwclZUBeHtxzoRTiXr0euAQeMI7gSntbMaePEQuh1Bc0F3Pu7JsNhXk7zPd', b'gAAAAABlSUQX50Sj8KNh0YHwP0R1p1muobx3tgdYjPHLieC7f4LFn4Svj-nRustJSr3fh5M9yT7JVnbYObECOQb1yzBXt2IrK4nIfX7TKRjH7TaG1TM5cZMl2u6Ls8hDQN3A3AOGdF_8', b'gAAAAABlSUfRe0TAbhXO7EzYCQwdvNkGupO18zaLLyVviKy1U7yxOesN3NH5Nc1JJ3YcQYm60GH8L_yzCCEdYh8ufIY3Jyt9sFSJUO5LLyCfBgvV7tA3HV6Mg0gVoJjkfQQcW1H1L-LR', b'gAAAAABlSUgv7mhXP1_WAzAVHNPlGepTljJs7Kj-9WP6OBF2pItVUu1-eBmwtwsc8Pm-lI1dCGNloc0uUtS8VjzjbTFGV1cp-RZxZrJyDUiu8Fi1Co2fhKLWzsEMQEd3UZ5VdImvYS59', b'gAAAAABlSUh-NALNLbpRuV6rhKPelNNpEKPr8sszrBgQktnFROM8fJ0wgzsK6UaA67gX6RIxyUJqdC8x3Dd6nPSPLt26ik76eYgvfTnJGZjsojb66nBS3KZG5fLbo4HoLlI07aE3KIbs', b'gAAAAABlSUjvcmcqf0wjrU9z3FaTxAsNL9A18nDtSzfOpNX5IHrjSfhDvXEf4iXcFqPx85RmPXh5QuUrlaPtnstgcmi4E6iGZfVn6ygoa-k5-TXnIQpCT_0LIEFb1JhZP6Kp1OKkpTde', b'gAAAAABlSUxQvOmFIhvH4upQFIZSD_elowL_ajvrr3bEUTLQ2NZdEua4OBpXnllU6lbBX6D7uclb8RV514nLCvY8AMW7JIM2HAPJltJFNpKmX3KnHo5T3rq_3HNSfaoiHxSm5uEUQpdtflwLeDsLb1EsALmEfAzC6g==', b'gAAAAABlSU4bf_ENQmObs3c5TSL9R74RfME1-ExmgyDRIliKS2UZ490CCmya6h3VVW_XVjDWWONSQXr8cca9W50mvjpmXPETzg==', b'gAAAAABlSU5Oi7Ee3RbvS1C76dDunuvse-larO-MRoHpcnbvl-77zDu2UEtVkzyr5V8tHtFhhr4HUUnkbPQIoQt323etNpHwjEvUvztV2RSXieKOF-GrIMiEz0Wp7kx1u6pyuMsOBNarvJvAwpo82cwQ9HlUwpmlkA==', b'gAAAAABlSU86Zg-AECHNPqi9gTliaBnJdWhF7J_K2-b98S7AKBcoqdfb3uxJ33sfw7zHUDheCU_NqHQ4vQNrmT7TlzgwvdwoFKa5_diiSKyxz-99H7JbsiX3Mr_ki9tS8IeyzfS-s7wL5ihe8zn-lqIgPxkNeYpPkg==', b'gAAAAABlSU9-ER0U_7YIyOCK7pl61Hbw9kofWbFkHacEt1MGuMXS81qsBkAFLdAZ1d4-X_WC2CDn5QZW_7H4pERmcvWf3_Qk7zvKXa0L7w_leZcp4fBBgi9PUnPmt0edcpG_RkrIjYQHwfmsjFPU3UrJGyWQk-uebJhq_Y1amKUgxdgSwUoyJZI=', b'gAAAAABlSU-_mW8noafKMxkYjzqtJ-x2b5c97q2C0S0UFJrwVrzUGGFWRyq5odDt8agdXdvsSbMzUKsKtX7VyM5HgdXntXXNZhtGQWrZ10Ew9hC3EM6gZ1_1POZqvQ2fVH_pO-HOgQG3wpjSkEMP8muc7OU9N7Yg46PKO5Jan6ikpAG55LGQq2K_aJDuvMWHKXhugNh4TwRm0LIPBTufg3jqeC-iOIyJlDRFKBoNy11WeQL-EpdxkY9iTMgrHlgZxhjdhJgtMuepRQEKZI70y2PgaNLIugp_iA==', b'gAAAAABlSVACXb0-O5EmT484XT3eyxuXbpCPTEr3xie4WIpUVTggtTWqA6mB7NZw5xNPMT0kcSmK7P-5siDtqCZTPJThyzaxxiSK1cD7kT4ulPm8riD_lvhYg0rcZzIL05OMHy5TLNokUXsL-iiMZ1DnGPXzsalbgqYmwcz-bViHEcup6SZybToxohnOpr9U5UHzYgLl77DlMQ0eXbvIXQzN7TOLGkXHbYrtoBTtRoN9tCqmGA8vq0w=', b'gAAAAABlSVAcUtIgeDTaTMvzaFFjHkpwh7OGHX6NmR6we58oTTaHNqNylqGG8wzbgBIPQpIh8q4CLYPnq4rfr2W5RYGa3AbxISNSckqpF5Rkuj12ha1JFR9iT4AlEs_qd7mwICTPr5ymWtvi4Skxjg-2qX5f9aEIbIrqONdeE-rQ8foSrM5PHKsPc9jZkjKIHRg_TGXpu5an5-W7Rse1j16CO8c7rA9grpM7eDfdJjJatUMak6rItZVBcobIfncTjgT7U-JDtTTX', b'gAAAAABlSVA6xo6A5LPDkWPgspeFdot1e7SuXOhn1PqMXR0mhWdGRS5TAGGUitMsIY_5r-IKW9r6Hx-zGk9Q4JCw26JCEdndHO77n35bFfx7qXLQIFJFRLU=', b'gAAAAABlSVBYBMOuiy3HzXEtb1TAKpY_UHMEopei7HCl1tUIlNutyPIs70_RJmF7APY_j0hUipWYLuBf3mID6-woXZblXakv6DWDCADb1jHVgRPDHwNj6QVYxdat9M_jnFkc6SNSpUmQ', b'gAAAAABlSVB20vk7L-l5Ec9GJDFp8lZVzkV6WgLye4qTErMPY2oPmiMo3gOF4pXOz90xgGrr5Ow-VmOKbzvNd31Wo4loIuQ5wWxkLKT1F2B8t8RWfsa6MhfUayymCAcPFsU2t2i1IOFHf0SWVDKD7ECUdl4hIhHMqdcOkkZ6AZMTInvcLlczOqRuKE8dCBrDvdVeCQJdicpw', b'gAAAAABlSVC61rJ5w0Lxo4empdd8JdP9jzQqmuYQXBo2tvmCwXEMaMAV93JXq6RUXvO-_2Bfxmf5TUptPCyQcUQ6h1eMwr9XexaAGndePCbgIfB8bhT3JGNQYVUkKmjM-gFFNqnavipF54Yzz9DesQI8P3O1N5wPWfpTUPfKqTUEcv5Aadk2GxyAxzjdww0xe54_iELGZov7_Vqv2mse2rN-eqERMdW5Cg==', b'gAAAAABlSVIN-Y0ucfEuhnMbAj9DAX6qPRxNBFvkbxihX9azZlydqACsgtOylK4ipM7EdhiqmqGU3SkWl9sS2HjiYQAAOwhDlEJdeCbfKtOU0YZwRVxLN1m40dLGkoGjU2ml5UWoS_AVpKLWYizw0U_sea3uU2X6FUrhcWMSCLgVj81vMCWu6bOMJrijfyJXzqRzWI0nacEoIEQvpYZeoYI_TfmRD9Jwycq0Xv8MedtZLYtnFzyr35ZmQWrZzZd5D3fTXjP4uIQeTmZzyp3Ij1AzM1IY4dCnGGM_ZGEIVFU48kg6FI_cXOaxqRS4Cpt1Oy30y2fu2VBzb3efJn6Z4a7Wg4hjzJkInGN-9JajtxhCG2HJQTW-63u8u5SpWoQaOSQyfUFn8WW_ST0IqbEFf1Y8XtEaVw_rnoprqJezQIwWGrjkXaNqiTqyjR-nPwnFEqI-hZRJ0HTNF7EWBBg3_6UpzRmC1Kd3DekOshJeal0FIWduZmaboVY2KQYQYq8NVhxbEQniD5-6MkrWiHdh121PD8saburG2one63EoeMeH5tgUWt9Gw7w=', b'gAAAAABlSVUi1gRHFWhSCOVjOaDGjmE6oWT1NTH7KoswV81XQifRIq16PpzEPfHzFVow4WTkUFKHvuxrfnjPKJNqYFKaG1keZbtzsMDzYsoc_KpqPJVbC1LNgauCZleyzFGITg1VL6ve', b'gAAAAABlSVVKdRWLpa3W4dN_c0jpacnDxTHD6QOTVW_NskJYoZWQwO-K62B1vbcc32CK9CBbIxvAdziDYeAhUyqMY81915YLUQ==', b'gAAAAABlSVVPeDtT-yhSRjHkujc89F9A0iOltCUMDJyqAFrjwG6_p2u5z2nffCg_C1JRbSqiwxIIUQmMSKZYwFs1Dmkma6sHxw==', b'']
    
import time
import sys

def desencriptacio():
    text_desencriptat_88 = format(fernet.decrypt(encriptats[88]).decode())        
    for _ in range(3):
        sys.stdout.write(f"\r{text_desencriptat_88}   ")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write(f"\r{text_desencriptat_88}.  ")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write(f"\r{text_desencriptat_88}.. ")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write(f"\r{text_desencriptat_88}...")
        sys.stdout.flush()
        time.sleep(0.5)
    
    sys.stdout.write("\r" + " " * len(f"{text_desencriptat_88}") + "\r") 
    sys.stdout.flush()
    text_desencriptat_86 = format(fernet.decrypt(encriptats[86]).decode())        
    text_desencriptat_86 = f"{text_desencriptat_86}"
    text_desencriptat_86 = text_desencriptat_86.replace("\\n", "\n")

    print(text_desencriptat_86)
    

#text_desencriptat_0 = fernet.decrypt(encriptats[0]).decode()       
#text_desencriptat_1 = fernet.decrypt(encriptats[1]).decode()       
#text_desencriptat_2 = fernet.decrypt(encriptats[2]).decode()       
#text_desencriptat_3 = fernet.decrypt(encriptats[3]).decode()       
#text_desencriptat_4 = fernet.decrypt(encriptats[4]).decode()       


text_desencriptat_48 = format(fernet.decrypt(encriptats[48]).decode())        
text_desencriptat_49 = format(fernet.decrypt(encriptats[49]).decode())        
text_desencriptat_50 = format(fernet.decrypt(encriptats[50]).decode())        
text_desencriptat_51 = format(fernet.decrypt(encriptats[51]).decode())       
text_desencriptat_52 = format(fernet.decrypt(encriptats[52]).decode())        
text_desencriptat_53 = format(fernet.decrypt(encriptats[53]).decode())       
text_desencriptat_54 = format(fernet.decrypt(encriptats[54]).decode())       
text_desencriptat_55 = format(fernet.decrypt(encriptats[55]).decode())       
text_desencriptat_56 = format(fernet.decrypt(encriptats[56]).decode())       
text_desencriptat_57 = format(fernet.decrypt(encriptats[57]).decode())       
text_desencriptat_58 = format(fernet.decrypt(encriptats[58]).decode())        
text_desencriptat_59 = format(fernet.decrypt(encriptats[59]).decode())        
text_desencriptat_60 = format(fernet.decrypt(encriptats[60]).decode())        
text_desencriptat_61 = format(fernet.decrypt(encriptats[61]).decode())        
text_desencriptat_62 = format(fernet.decrypt(encriptats[62]).decode())       
text_desencriptat_63 = format(fernet.decrypt(encriptats[63]).decode())        
text_desencriptat_64 = format(fernet.decrypt(encriptats[64]).decode())        
text_desencriptat_65 = format(fernet.decrypt(encriptats[65]).decode())        

def desitjar_aniversari():
    import random
    
    text_desencriptat_0 = fernet.decrypt(encriptats[0]).decode()       
    text0 = text_desencriptat_0
    paraules1 = text0.split(", ")
    paraules1 = [exp.replace('"', '') for exp in paraules1]
    
    text_desencriptat_1 = fernet.decrypt(encriptats[1]).decode()       
    text1 = text_desencriptat_1
    paraules2 = text1.split(", ")
    paraules2 = [exp.replace('"', '') for exp in paraules2]
    
    text_desencriptat_2 = fernet.decrypt(encriptats[2]).decode()       
    text2 = text_desencriptat_2
    paraules3 = text2.split(", ")
    paraules3 = [exp.replace('"', '') for exp in paraules3]
    
    text_desencriptat_3 = fernet.decrypt(encriptats[3]).decode()       
    text3 = text_desencriptat_3
    paraules4 = text3.split(", ")
    paraules4 = [exp.replace('"', '') for exp in paraules4]
    
    text_desencriptat_4 = fernet.decrypt(encriptats[4]).decode()       
    text4 = text_desencriptat_4
    paraules5 = text4.split(", ")
    paraules5 = [exp.replace('"', '') for exp in paraules5]
    
    paraula1 = random.choice(paraules1)
    paraula2 = random.choice(paraules2)
    paraula3 = random.choice(paraules3)
    paraula4 = random.choice(paraules4)
    paraula5 = random.choice(paraules5)

    text_desencriptat_85 = format(fernet.decrypt(encriptats[85]).decode())       
    text_desencriptat_85 = f"{text_desencriptat_85}"
    text_desencriptat_85 = text_desencriptat_85.replace("\\n", "\n")
    text_desencriptat_85 = text_desencriptat_85.replace("{resposta}", resposta)
    text_desencriptat_85 = text_desencriptat_85.replace("{resposta2}", resposta2)
    text_desencriptat_85 = text_desencriptat_85.replace("{resposta3}", resposta3)
    text_desencriptat_85 = text_desencriptat_85.replace("{paraula1}", paraula1)
    text_desencriptat_85 = text_desencriptat_85.replace("{paraula2}", paraula2)
    text_desencriptat_85 = text_desencriptat_85.replace("{paraula3}", paraula3)
    text_desencriptat_85 = text_desencriptat_85.replace("{paraula4}", paraula4)
    text_desencriptat_85 = text_desencriptat_85.replace("{paraula5}", paraula5)

    missatge = text_desencriptat_85
    print(missatge)
            
text_desencriptat_5 = format(fernet.decrypt(encriptats[5]).decode())        
text_desencriptat_5 = f"{text_desencriptat_5}"
text_desencriptat_5 = text_desencriptat_5.replace("\\n", "\n")

desencriptacio()
print(text_desencriptat_5)

while True:
    resposta = input()

    if resposta == text_desencriptat_50:
        text_desencriptat_6 = format(fernet.decrypt(encriptats[6]).decode())     
        text_desencriptat_6 = f"{text_desencriptat_6}"
        text_desencriptat_6 = text_desencriptat_6.replace("\\n", "\n")
        print(text_desencriptat_6)

        text_desencriptat_7 = format(fernet.decrypt(encriptats[7]).decode())        
        text_desencriptat_7 = f"{text_desencriptat_7}"
        text_desencriptat_7 = text_desencriptat_7.replace("\\n", "\n")
        print(text_desencriptat_7)

        while True:
            resposta = input()

            if resposta == text_desencriptat_49:
                print(text_desencriptat_6)

                text_desencriptat_8 = format(fernet.decrypt(encriptats[8]).decode())        
                text_desencriptat_8 = f"{text_desencriptat_8}"
                text_desencriptat_8 = text_desencriptat_8.replace("\\n", "\n")

                resposta = input(text_desencriptat_8)

                while True:
                    text_desencriptat_9 = format(fernet.decrypt(encriptats[9]).decode())        
                    text_desencriptat_9 = f"{text_desencriptat_9}"
                    text_desencriptat_9 = text_desencriptat_9.replace("\\n", "\n")
                    resposta1 = input(text_desencriptat_9.format(resposta, resposta))

                    if resposta1 == text_desencriptat_49:
                        text_desencriptat_76 = format(fernet.decrypt(encriptats[76]).decode())       
                        text_desencriptat_76 = f"{text_desencriptat_76}"
                        text_desencriptat_76 = text_desencriptat_76.replace("\\n", "\n")
                        text_desencriptat_76 = text_desencriptat_76.replace("{resposta}", resposta)
                        print(text_desencriptat_76)
                        
                        text_desencriptat_77 = format(fernet.decrypt(encriptats[77]).decode())      
                        text_desencriptat_77 = f"{text_desencriptat_77}"
                        text_desencriptat_77 = text_desencriptat_77.replace("\\n", "\n")
                        text_desencriptat_77 = text_desencriptat_77.replace("{resposta}", resposta)
                        resposta2 = input(text_desencriptat_77)
                        text_desencriptat_78 = format(fernet.decrypt(encriptats[78]).decode())       
                        text_desencriptat_78 = f"{text_desencriptat_78}"
                        text_desencriptat_78 = text_desencriptat_78.replace("\\n", "\n")
                        text_desencriptat_78 = text_desencriptat_78.replace("{resposta}", resposta)
                        text_desencriptat_78 = text_desencriptat_78.replace("{resposta2}", resposta2)
                        resposta3 = input(text_desencriptat_78)

                        correm = True
                        while correm == True:
                            text_desencriptat_79 = format(fernet.decrypt(encriptats[79]).decode())        
                            text_desencriptat_79 = f"{text_desencriptat_79}"
                            text_desencriptat_79 = text_desencriptat_79.replace("\\n", "\n")
                            text_desencriptat_79 = text_desencriptat_79.replace("{resposta}", resposta)
                            text_desencriptat_79 = text_desencriptat_79.replace("{resposta2}", resposta2)
                            text_desencriptat_79 = text_desencriptat_79.replace("{resposta3}", resposta3)
                            resposta4 = input(text_desencriptat_79)

                            if resposta4 == text_desencriptat_48:
    
                                text_desencriptat_10 = format(fernet.decrypt(encriptats[10]).decode())        
                                text_desencriptat_10 = f"{text_desencriptat_10}"
                                text_desencriptat_10 = text_desencriptat_10.replace("\\n", "\n")

                                
                                lloc = input(text_desencriptat_10)

                                while True:
                                    if lloc == text_desencriptat_58:
                                        
                                        text_desencriptat_80 = format(fernet.decrypt(encriptats[80]).decode())        
                                        text_desencriptat_80 = f"{text_desencriptat_80}"
                                        text_desencriptat_80 = text_desencriptat_80.replace("\\n", "\n")
                                        text_desencriptat_80 = text_desencriptat_80.replace("{resposta}", resposta)
                                        text_desencriptat_80 = text_desencriptat_80.replace("{resposta2}", resposta2)
                                        text_desencriptat_80 = text_desencriptat_80.replace("{resposta3}", resposta3)

                                        print(text_desencriptat_80)
                                        
                                        text_desencriptat_11 = format(fernet.decrypt(encriptats[11]).decode())        
                                        text_desencriptat_11 = f"{text_desencriptat_11}"
                                        text_desencriptat_11 = text_desencriptat_11.replace("\\n", "\n")
 
                                        dia = input(text_desencriptat_11)

                                        while True:
                                            if dia == text_desencriptat_59:
                                                bucles = True
                                                while bucles == True:
                                                    text_desencriptat_81 = format(fernet.decrypt(encriptats[81]).decode())       
                                                    text_desencriptat_81 = f"{text_desencriptat_81}"
                                                    text_desencriptat_81 = text_desencriptat_81.replace("\\n", "\n")
                                                    text_desencriptat_81 = text_desencriptat_81.replace("{dia}", dia)

                                                    confirmacio = input(text_desencriptat_81)

                                                    if confirmacio == text_desencriptat_49:
                                                        while True:
                                                                text_desencriptat_82 = format(fernet.decrypt(encriptats[82]).decode())        
                                                                text_desencriptat_82 = f"{text_desencriptat_82}"
                                                                text_desencriptat_82 = text_desencriptat_82.replace("\\n", "\n")
                                                                text_desencriptat_82 = text_desencriptat_82.replace("{dia}", dia)

                                                                confirmacio2 = input(text_desencriptat_82)
                                                                if confirmacio2 == text_desencriptat_49:
                                                                    while True:
                                                                        text_desencriptat_83 = format(fernet.decrypt(encriptats[83]).decode())       
                                                                        text_desencriptat_83 = f"{text_desencriptat_83}"
                                                                        text_desencriptat_83 = text_desencriptat_83.replace("\\n", "\n")
                                                                        text_desencriptat_83 = text_desencriptat_83.replace("{resposta}", resposta)
                                                                        text_desencriptat_83 = text_desencriptat_83.replace("{resposta2}", resposta2)
                                                                        text_desencriptat_83 = text_desencriptat_83.replace("{resposta3}", resposta3)
                                                                        text_desencriptat_83 = text_desencriptat_83.replace("{dia}", dia)
                                                                        
                                                                        confirmacio3 = input(text_desencriptat_83)
                                                                        if confirmacio3 == text_desencriptat_49:
                                                                            import time
                                                                            text_desencriptat_12 = format(fernet.decrypt(encriptats[12]).decode())        
                                                                            text_desencriptat_12 = f"{text_desencriptat_12}"
                                                                            text_desencriptat_12 = text_desencriptat_12.replace("\\n", "\n")
                                                                            print(text_desencriptat_12)
                                                                            time.sleep(2)
                                                                            print(f"{resposta}")
                                                                            time.sleep(1)
                                                                            print(f"{resposta2}")
                                                                            time.sleep(1)
                                                                            print(f"{resposta3}")
                                                                            time.sleep(1)
                                                                            text_desencriptat_43 = format(fernet.decrypt(encriptats[43]).decode())        
                                                                            print(text_desencriptat_43)
                                                                            time.sleep(1)
                                                                            text_desencriptat_45 = format(fernet.decrypt(encriptats[45]).decode())        
                                                                            print(text_desencriptat_45)
                                                                            time.sleep(1)
                                                                            text_desencriptat_46 = format(fernet.decrypt(encriptats[46]).decode())        
                                                                            print(text_desencriptat_46)
                                                                            time.sleep(1)
                                                                            print("!")
                                                                            time.sleep(1)
                                                                            print("!")                
                                                                            time.sleep(1)
                                                                            print("!")                
                                                                            time.sleep(2)   
                                                                            text_desencriptat_13 = format(fernet.decrypt(encriptats[13]).decode())        
                                                                            text_desencriptat_13 = f"{text_desencriptat_13}"
                                                                            text_desencriptat_13 = text_desencriptat_13.replace("\\n", "\n")
                                                                            
                                                                            final = input(text_desencriptat_13)
                                                                            if final == text_desencriptat_49:
                                                                                desitjar_aniversari()
                                                                                while True:
                                                                                    text_desencriptat_14 = format(fernet.decrypt(encriptats[14]).decode())       
                                                                                    text_desencriptat_14 = f"{text_desencriptat_14}"
                                                                                    text_desencriptat_14 = text_desencriptat_14.replace("\\n", "\n")
                                                                                    final2 = input(text_desencriptat_14)
                                                                                    if final2 == text_desencriptat_49:
                                                                                        text_desencriptat_47 = format(fernet.decrypt(encriptats[47]).decode())        
                                                                                        print(text_desencriptat_47)
                                                                                        desitjar_aniversari()

                                                                                    elif final2 == text_desencriptat_48:
                                                                                        text_desencriptat_15 = format(fernet.decrypt(encriptats[15]).decode())      
                                                                                        text_desencriptat_15 = f"{text_desencriptat_15}"
                                                                                        text_desencriptat_15 = text_desencriptat_15.replace("\\n", "\n")
                                                                                        print(text_desencriptat_15)
                                                                                        break

                                                                                    else:
                                                                                        text_desencriptat_16 = format(fernet.decrypt(encriptats[16]).decode())        
                                                                                        text_desencriptat_16 = f"{text_desencriptat_16}"
                                                                                        text_desencriptat_16 = text_desencriptat_16.replace("\\n", "\n")
                                                                                        print(text_desencriptat_16)


                                                                            else:
                                                                                text_desencriptat_42 = format(fernet.decrypt(encriptats[42]).decode())        
                                                                                text_desencriptat_42 = f"{text_desencriptat_42}"
                                                                                text_desencriptat_42 = text_desencriptat_42.replace("\\n", "\n")
                                                                                print(text_desencriptat_42)
                                                                                desitjar_aniversari()
                                                                                while True:
                                                                                    text_desencriptat_41 = format(fernet.decrypt(encriptats[41]).decode())      
                                                                                    text_desencriptat_41 = f"{text_desencriptat_41}"
                                                                                    text_desencriptat_41 = text_desencriptat_41.replace("\\n", "\n")
                                                                                    final3 = input(text_desencriptat_41)
                                                                                    if final3 == text_desencriptat_49:
                                                                                        text_desencriptat_47 = format(fernet.decrypt(encriptats[47]).decode())       
                                                                                        print(text_desencriptat_47)
                                                                                        desitjar_aniversari()

                                                                                    elif final3 == text_desencriptat_48:
                                                                                        text_desencriptat_40 = format(fernet.decrypt(encriptats[40]).decode())        
                                                                                        text_desencriptat_40 = f"{text_desencriptat_40}"
                                                                                        text_desencriptat_40 = text_desencriptat_40.replace("\\n", "\n")
                                                                                        print(text_desencriptat_40)
                                                                                        break

                                                                                    else:
                                                                                        text_desencriptat_16 = format(fernet.decrypt(encriptats[16]).decode())        
                                                                                        text_desencriptat_16 = f"{text_desencriptat_16}"
                                                                                        text_desencriptat_16 = text_desencriptat_16.replace("\\n", "\n")
                                                                                        print(text_desencriptat_16)                                                                            
                                                                            break

                                                                        else:
                                                                            text_desencriptat_39 = format(fernet.decrypt(encriptats[39]).decode())       
                                                                            text_desencriptat_39 = f"{text_desencriptat_39}"
                                                                            text_desencriptat_39 = text_desencriptat_39.replace("\\n", "\n")
                                                                            print(text_desencriptat_39)
                                                                    break
                                                                else:
                                                                    text_desencriptat_39 = format(fernet.decrypt(encriptats[39]).decode())        
                                                                    text_desencriptat_39 = f"{text_desencriptat_39}"
                                                                    text_desencriptat_39 = text_desencriptat_39.replace("\\n", "\n")
                                                                    print(text_desencriptat_39)
                                                        break

                                                    elif confirmacio == text_desencriptat_48:
                                                        text_desencriptat_38 = format(fernet.decrypt(encriptats[38]).decode())        
                                                        text_desencriptat_38 = f"{text_desencriptat_38}"
                                                        text_desencriptat_38 = text_desencriptat_38.replace("\\n", "\n")
                                                        print(text_desencriptat_38)
                                                        break

                                                    else:
                                                        text_desencriptat_16 = format(fernet.decrypt(encriptats[16]).decode())       
                                                        text_desencriptat_16 = f"{text_desencriptat_16}"
                                                        text_desencriptat_16 = text_desencriptat_16.replace("\\n", "\n")
                                                        print(text_desencriptat_16)
            
                                                if confirmacio == text_desencriptat_48:
                                                    dia = input()

                                                else:
                                                    break

                                            elif dia == text_desencriptat_60:
                                                text_desencriptat_37 = format(fernet.decrypt(encriptats[37]).decode())        
                                                text_desencriptat_37 = f"{text_desencriptat_37}"
                                                text_desencriptat_37 = text_desencriptat_37.replace("\\n", "\n")
                                                print(text_desencriptat_37)
                                                dia = input()

                                            elif dia == text_desencriptat_61:
                                                text_desencriptat_36 = format(fernet.decrypt(encriptats[36]).decode())        
                                                text_desencriptat_36 = f"{text_desencriptat_36}"
                                                text_desencriptat_36 = text_desencriptat_36.replace("\\n", "\n")
                                                print(text_desencriptat_36)
                                                dia = input()

                                            elif dia == text_desencriptat_62:
                                                text_desencriptat_35 = format(fernet.decrypt(encriptats[35]).decode())        
                                                text_desencriptat_35 = f"{text_desencriptat_35}"
                                                text_desencriptat_35 = text_desencriptat_35.replace("\\n", "\n")
                                                print(text_desencriptat_35)
                                                dia = input()

                                            elif dia == text_desencriptat_63:
                                                text_desencriptat_34 = format(fernet.decrypt(encriptats[34]).decode())       
                                                text_desencriptat_34 = f"{text_desencriptat_34}"
                                                text_desencriptat_34 = text_desencriptat_34.replace("\\n", "\n")
                                                print(text_desencriptat_34)
                                                dia = input()

                                            elif dia == text_desencriptat_64:
                                                text_desencriptat_33 = format(fernet.decrypt(encriptats[33]).decode())        
                                                text_desencriptat_33 = f"{text_desencriptat_33}"
                                                text_desencriptat_33 = text_desencriptat_33.replace("\\n", "\n")
                                                print(text_desencriptat_33)
                                                dia = input()

                                            elif dia == text_desencriptat_65:
                                                text_desencriptat_32 = format(fernet.decrypt(encriptats[32]).decode())       
                                                text_desencriptat_32 = f"{text_desencriptat_32}"
                                                text_desencriptat_32 = text_desencriptat_32.replace("\\n", "\n")
                                                print(text_desencriptat_32)
                                                dia = input()

                                            else:
                                                text_desencriptat_31 = format(fernet.decrypt(encriptats[31]).decode())        
                                                text_desencriptat_31 = f"{text_desencriptat_31}"
                                                text_desencriptat_31 = text_desencriptat_31.replace("\\n", "\n")
                                                print(text_desencriptat_31)
                                                text_desencriptat_30 = format(fernet.decrypt(encriptats[30]).decode())        
                                                text_desencriptat_30 = f"{text_desencriptat_30}"
                                                text_desencriptat_30 = text_desencriptat_30.replace("\\n", "\n")
                                                dia = input(text_desencriptat_30)
                                        break

                                    else:
                                        text_desencriptat_29 = format(fernet.decrypt(encriptats[29]).decode())      
                                        text_desencriptat_29 = f"{text_desencriptat_29}"
                                        text_desencriptat_29 = text_desencriptat_29.replace("\\n", "\n")
                                        print(text_desencriptat_29)
                                        lloc = input()
                                break

                            elif resposta4 == text_desencriptat_49:
                                while True:
                                    text_desencriptat_27 = format(fernet.decrypt(encriptats[27]).decode())       
                                    text_desencriptat_27 = f"{text_desencriptat_27}"
                                    text_desencriptat_27 = text_desencriptat_27.replace("\\n", "\n")
                                    motiu = input(text_desencriptat_27)
                                    
                                    text_desencriptat_28 = format(fernet.decrypt(encriptats[28]).decode())       
                                    text_desencriptat_28 = f"{text_desencriptat_28}"
                                    text_desencriptat_28 = text_desencriptat_28.replace("\\n", "\n")
                                    resposta5 = input(text_desencriptat_28)
                                    
                                    if resposta5 == text_desencriptat_48:
                                        text_desencriptat_26 = format(fernet.decrypt(encriptats[26]).decode())      
                                        text_desencriptat_26 = f"{text_desencriptat_26}"
                                        text_desencriptat_26 = text_desencriptat_26.replace("\\n", "\n")
                                        print(text_desencriptat_26)
                                        correm = False
                                        break
                                    elif resposta5 == text_desencriptat_49:
                                        text_desencriptat_25 = format(fernet.decrypt(encriptats[25]).decode())     
                                        text_desencriptat_25 = f"{text_desencriptat_25}"
                                        text_desencriptat_25 = text_desencriptat_25.replace("\\n", "\n")
                                        print(text_desencriptat_25)
                                        break
                                    else:
                                        text_desencriptat_16 = format(fernet.decrypt(encriptats[16]).decode())        
                                        text_desencriptat_16 = f"{text_desencriptat_16}"
                                        text_desencriptat_16 = text_desencriptat_16.replace("\\n", "\n")
                                        print(text_desencriptat_16)                                        
                            else:
                                text_desencriptat_16 = format(fernet.decrypt(encriptats[16]).decode())       
                                text_desencriptat_16 = f"{text_desencriptat_16}"
                                text_desencriptat_16 = text_desencriptat_16.replace("\\n", "\n")
                                print(text_desencriptat_16)

                        break

                    elif resposta1 == text_desencriptat_48:
                        text_desencriptat_84 = format(fernet.decrypt(encriptats[84]).decode())       
                        text_desencriptat_84 = f"{text_desencriptat_84}"
                        text_desencriptat_84 = text_desencriptat_84.replace("\\n", "\n")
                        text_desencriptat_84 = text_desencriptat_84.replace("{resposta}", resposta)

                        print(text_desencriptat_84)
                        break

                    else:
                                text_desencriptat_16 = format(fernet.decrypt(encriptats[16]).decode())       
                                text_desencriptat_16 = f"{text_desencriptat_16}"
                                text_desencriptat_16 = text_desencriptat_16.replace("\\n", "\n")
                                print(text_desencriptat_16)
                break

            elif resposta == text_desencriptat_57:
                text_desencriptat_17 = format(fernet.decrypt(encriptats[17]).decode())        
                text_desencriptat_17 = f"{text_desencriptat_17}"
                text_desencriptat_17 = text_desencriptat_17.replace("\\n", "\n")
                print(text_desencriptat_17)  

            elif resposta == text_desencriptat_56:
                text_desencriptat_17 = format(fernet.decrypt(encriptats[17]).decode())       
                text_desencriptat_17 = f"{text_desencriptat_17}"
                text_desencriptat_17 = text_desencriptat_17.replace("\\n", "\n")
                print(text_desencriptat_17)  

            elif resposta == text_desencriptat_55:
                text_desencriptat_18 = format(fernet.decrypt(encriptats[18]).decode())    
                text_desencriptat_18 = f"{text_desencriptat_18}"
                text_desencriptat_18 = text_desencriptat_18.replace("\\n", "\n")
                print(text_desencriptat_18)  

            elif resposta == text_desencriptat_54:
                text_desencriptat_20 = format(fernet.decrypt(encriptats[20]).decode())       
                text_desencriptat_20 = f"{text_desencriptat_20}"
                text_desencriptat_20 = text_desencriptat_20.replace("\\n", "\n")
                print(text_desencriptat_20)

            elif resposta == text_desencriptat_53:
                text_desencriptat_17 = format(fernet.decrypt(encriptats[17]).decode())      
                text_desencriptat_17 = f"{text_desencriptat_17}"
                text_desencriptat_17 = text_desencriptat_17.replace("\\n", "\n")
                print(text_desencriptat_17)   

            elif resposta == text_desencriptat_52:
                text_desencriptat_17 = format(fernet.decrypt(encriptats[17]).decode())      
                text_desencriptat_17 = f"{text_desencriptat_17}"
                text_desencriptat_17 = text_desencriptat_17.replace("\\n", "\n")
                print(text_desencriptat_17)  

            elif resposta == text_desencriptat_48:
                text_desencriptat_21 = format(fernet.decrypt(encriptats[21]).decode())     
                text_desencriptat_21 = f"{text_desencriptat_21}"
                text_desencriptat_21 = text_desencriptat_21.replace("\\n", "\n")
                print(text_desencriptat_21)

            else:
                text_desencriptat_22 = format(fernet.decrypt(encriptats[22]).decode())    
                text_desencriptat_22 = f"{text_desencriptat_22}"
                text_desencriptat_22 = text_desencriptat_22.replace("\\n", "\n")
                print(text_desencriptat_22)
        break

    elif resposta == text_desencriptat_51:
        text_desencriptat_23 = format(fernet.decrypt(encriptats[23]).decode())     
        text_desencriptat_23 = f"{text_desencriptat_23}"
        text_desencriptat_23 = text_desencriptat_23.replace("\\n", "\n")
        print(text_desencriptat_23)
        break  

    else:
        text_desencriptat_24 = format(fernet.decrypt(encriptats[24]).decode())        
        text_desencriptat_24 = f"{text_desencriptat_24}"
        text_desencriptat_24 = text_desencriptat_24.replace("\\n", "\n")
        print(text_desencriptat_24)