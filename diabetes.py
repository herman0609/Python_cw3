import csv
def generate_summary_for_web(csvfile, html_title, html_filename, show_barchart_gender=True):
    def picture(csvfile):
        try:
            with open(csvfile) as file:
                sh = csv.reader(file)
                data = []
                data = [row for row in sh]
                data.remove(data[0])
        except FileNotFoundError:
            raise FileNotFoundError
        
        m_list = []
        f_list = []
        for row in data:
            if row[1] == "Male":
                m_list.append(row)
            if row[1] == "Female":
                f_list.append(row)
        mp = []
        fp = []
        mn = []
        fn = []
        for row in m_list:
            if row[-1] == "Positive":
                mp.append(row)
            if row[-1] == "Negative":
                mn.append(row)
        for row in f_list:
            if row[-1] == "Positive":
                fp.append(row)
            if row[-1] == "Negative":
                fn.append(row)

        from matplotlib import pyplot as plt


        a = ["Positive","Negative"]
        sh = [len(mp), len(mn)]
        sh1 = [len(fp), len(fn)]
        bar_width = 0.4
         
        b = list(range(len(a)))
        x_15 = [i + bar_width for i in b]
        hg = [0.2, 1.2]
        
        plt.rcParams['axes.facecolor']='#84AF9B'
        font={"family":"SimHei","style":"italic","weight":"bold","color":"black","size":25}
        font1={"family":"impact","style":"normal","weight":"bold","color":"black","size":40}
        font2={"family":"verdana","style":"normal","weight":"normal","color":"r","size":20}

        plt.figure(figsize=(15,15),dpi=80)
        
        for x1, y1, y2 in zip(b, sh, sh1):
            plt.text(x1, y1, "%d"%y1, ha = "center", fontdict=font2)
            plt.text(x1+bar_width, y2, "%d"%y2, ha = "center", fontdict=font2)
            
        plt.grid(True,color="g",axis="y",ls="-.",lw=1)

        plt.bar(range(len(a)), sh, width=bar_width, label="Male", color='gray', alpha=1, edgecolor="k", hatch='***')
        plt.bar(x_15, sh1, width=bar_width, label="Female", color='white', alpha=1, edgecolor="k", hatch="xxx")
        plt.xlabel('Class\n', fontdict=font)
        plt.ylabel('Count\n', fontdict=font)
        plt.title('Gender of Positive vs Negatives case\n', fontdict=font1)

        plt.legend(fontsize = 30)

        plt.xticks(hg, a, fontsize = 20)
        plt.yticks(fontsize = 20)
        plt.savefig(fname="barchart.png")
    
    header = []
    data = []
    try:
        with open(csvfile) as file:
            sh = csv.reader(file)
            try:
                header = next(sh)
            except:
                header = None
            data = [row for row in sh]
            header.remove(header[0])
            header.remove(header[0])
            header.remove(header[-1])
    except FileNotFoundError:
        header = None
        raise FileNotFoundError

    data1 = []
    data2 = []
    yn1 = []
    yn2 = []
    yn3 = []
    yn4 = []
    yn5 = []
    yn6 = []
    yn7 = []
    yn8 = []
    yn9 = []
    yn10 = []
    yn11 = []
    yn12 = []
    yn13 = []
    yn14 = []

    syn1 = []
    syn2 = []
    syn3 = []
    syn4 = []
    syn5 = []
    syn6 = []
    syn7 = []
    syn8 = []
    syn9 = []
    syn10 = []
    syn11 = []
    syn12 = []
    syn13 = []
    syn14 = []
    for col in data:
        if col[-1] == "Positive":
            data1.append(col)
    for col in data:
        if col[-1] == "Negative":
            data2.append(col)
    for col in data1:
        col.remove(col[0])
        col.remove(col[0])
        col.remove(col[-1])
    for col in data2:
        col.remove(col[0])
        col.remove(col[0])
        col.remove(col[-1])
    for col in data1:
        yn1.append(col[0])
        col.remove(col[0])
        yn2.append(col[0])
        col.remove(col[0])
        yn3.append(col[0])
        col.remove(col[0])
        yn4.append(col[0])
        col.remove(col[0])
        yn5.append(col[0])
        col.remove(col[0])
        yn6.append(col[0])
        col.remove(col[0])
        yn7.append(col[0])
        col.remove(col[0])
        yn8.append(col[0])
        col.remove(col[0])
        yn9.append(col[0])
        col.remove(col[0])
        yn10.append(col[0])
        col.remove(col[0])
        yn11.append(col[0])
        col.remove(col[0])
        yn12.append(col[0])
        col.remove(col[0])
        yn13.append(col[0])
        col.remove(col[0])
        yn14.append(col[0])
        col.remove(col[0])
        
    for col in data2:
        syn1.append(col[0])
        col.remove(col[0])
        syn2.append(col[0])
        col.remove(col[0])
        syn3.append(col[0])
        col.remove(col[0])
        syn4.append(col[0])
        col.remove(col[0])
        syn5.append(col[0])
        col.remove(col[0])
        syn6.append(col[0])
        col.remove(col[0])
        syn7.append(col[0])
        col.remove(col[0])
        syn8.append(col[0])
        col.remove(col[0])
        syn9.append(col[0])
        col.remove(col[0])
        syn10.append(col[0])
        col.remove(col[0])
        syn11.append(col[0])
        col.remove(col[0])
        syn12.append(col[0])
        col.remove(col[0])
        syn13.append(col[0])
        col.remove(col[0])
        syn14.append(col[0])
        col.remove(col[0])
    
    num = 0
    num1 = 0
    for ele in yn1:
        if ele == "Yes":
            num += 1
        if ele == "No":
            num1 += 1
    
    num2 = 0
    num3 = 0
    for ele in yn2:
        if ele == "Yes":
            num2 += 1
        if ele == "No":
            num3 += 1
    
    num4 = 0
    num5 = 0
    for ele in yn3:
        if ele == "Yes":
            num4 += 1
        if ele == "No":
            num5 += 1
    
    num6 = 0
    num7 = 0
    for ele in yn4:
        if ele == "Yes":
            num6 += 1
        if ele == "No":
            num7 += 1

    num8 = 0
    num9 = 0
    for ele in yn5:
        if ele == "Yes":
            num8 += 1
        if ele == "No":
            num9 += 1

    num10 = 0
    num11 = 0
    for ele in yn6:
        if ele == "Yes":
            num10 += 1
        if ele == "No":
            num11 += 1

    num12 = 0
    num13 = 0
    for ele in yn7:
        if ele == "Yes":
            num12 += 1
        if ele == "No":
            num13 += 1
    
    num14 = 0
    num15 = 0
    for ele in yn8:
        if ele == "Yes":
            num14 += 1
        if ele == "No":
            num15 += 1

    num16 = 0
    num17 = 0
    for ele in yn9:
        if ele == "Yes":
            num16 += 1
        if ele == "No":
            num17 += 1

    num18 = 0
    num19 = 0
    for ele in yn10:
        if ele == "Yes":
            num18 += 1
        if ele == "No":
            num19 += 1

    num20 = 0
    num21 = 0
    for ele in yn11:
        if ele == "Yes":
            num20 += 1
        if ele == "No":
            num21 += 1
    
    num22 = 0
    num23 = 0
    for ele in yn12:
        if ele == "Yes":
            num22 += 1
        if ele == "No":
            num23 += 1

    num24 = 0
    num25 = 0
    for ele in yn13:
        if ele == "Yes":
            num24 += 1
        if ele == "No":
            num25 += 1

    num26 = 0
    num27 = 0
    for ele in yn14:
        if ele == "Yes":
            num26 += 1
        if ele == "No":
            num27 += 1


    um = 0
    um1 = 0
    for ele in syn1:
        if ele == "Yes":
            um += 1
        if ele == "No":
            um1 += 1
    
    um2 = 0
    um3 = 0
    for ele in syn2:
        if ele == "Yes":
            um2 += 1
        if ele == "No":
            um3 += 1

    um4 = 0
    um5 = 0
    for ele in syn3:
        if ele == "Yes":
            um4 += 1
        if ele == "No":
            um5 += 1

    um6 = 0
    um7 = 0
    for ele in syn4:
        if ele == "Yes":
            um6 += 1
        if ele == "No":
            um7 += 1
            
    um8 = 0
    um9 = 0
    for ele in syn5:
        if ele == "Yes":
            um8 += 1
        if ele == "No":
            um9 += 1
            
    um10 = 0
    um11 = 0
    for ele in syn6:
        if ele == "Yes":
            um10 += 1
        if ele == "No":
            um11 += 1
            
    um12 = 0
    um13 = 0
    for ele in syn7:
        if ele == "Yes":
            um12 += 1
        if ele == "No":
            um13 += 1
            
    um14 = 0
    um15 = 0
    for ele in syn8:
        if ele == "Yes":
            um14 += 1
        if ele == "No":
            um15 += 1
            
    um16 = 0
    um17 = 0
    for ele in syn9:
        if ele == "Yes":
            um16 += 1
        if ele == "No":
            um17 += 1
            
    um18 = 0
    um19 = 0
    for ele in syn10:
        if ele == "Yes":
            um18 += 1
        if ele == "No":
            um19 += 1
            
    um20 = 0
    um21 = 0
    for ele in syn11:
        if ele == "Yes":
            um20 += 1
        if ele == "No":
            um21 += 1
            
    um22 = 0
    um23 = 0
    for ele in syn12:
        if ele == "Yes":
            um22 += 1
        if ele == "No":
            um23 += 1
            
    um24 = 0
    um25 = 0
    for ele in syn13:
        if ele == "Yes":
            um24 += 1
        if ele == "No":
            um25 += 1
            
    um26 = 0
    um27 = 0
    for ele in syn14:
        if ele == "Yes":
            um26 += 1
        if ele == "No":
            um27 += 1
            

    with open(html_filename ,"w") as html:
        html.write("<html>\n")
        html.write("<head>\n")
        html.write("<meta charset=\"UTF-8\">\n")
        #style
        html.write("<style type='text/css'>\n")
        html.write("table{\
				margin-left: 42%;\
				margin-top: 80px;\
			}\
                caption{\
				font-size: 2em;\
				margin-bottom: 15px;\
				font-family: verdana;\
				font-weight: bold;\
			}\
            table.altrowstable {\
            font-family: verdana,arial,sans-serif;\
			    font-size:11px;\
			    color:#333333;\
			    border-width: 1px;\
			    border-color: #a9c6c9;\
			    border-collapse: collapse;\
			}\
			table.altrowstable th {\
			    border-width: 1px;\
			    padding: 8px;\
			    border-style: solid;\
			    border-color: #a9c6c9;\
			}\
			table.altrowstable td {\
			    border-width: 1px;\
			    padding: 8px;\
			    border-style: solid;\
			    border-color: #a9c6c9;\
			}\
			.oddrowcolor{\
			    background-color:#d4e3e5;\
			}\
			.evenrowcolor{\
			    background-color:#c3dde0;\
			}\
			#picture{\
            margin-top: 100px;\
            text-align: center;\
            overflow: hidden;\
            margin-top: 30px;\
			}\
			#picture img{\
				cursor: pointer;\
				transition: all 0.6s;\
			}\
			#picture img:hover{\
				transform: scale(1.1);\
			}")
        html.write("</style>\n")

        html.write("<script type='text/javascript'>\n")
        html.write("\t\tfunction altRows(id){\n")
        html.write("\t\t\tif(document.getElementsByTagName){\n")
        html.write("\t\t\t\tvar table = document.getElementById(id);\n")
        html.write("\t\t\t\tvar rows = table.getElementsByTagName('tr');\n")
        html.write("\n")
        html.write("\t\t\t\tfor(i = 0; i < rows.length; i++){\n")
        html.write("\t\t\t\t\tif(i % 2 == 0){\n")
        html.write("\t\t\t\t\t\trows[i].className = 'evenrowcolor';\n")
        html.write("\t\t\t\t\t}else{\n")
        html.write("\t\t\t\t\t\trows[i].className = 'oddrowcolor';\n")
        html.write("\t\t\t\t\t}\n")
        html.write("\t\t\t\t}\n")
        html.write("\t\t\t}\n")
        html.write("\t\t}\n")
        html.write("\n")
        html.write("\t\twindow.onload=function(){\n")
        html.write("\t\t\taltRows('alternatecolor');\n")
        html.write("\t\t}\n")
        html.write("\n")
        html.write("</script>\n")
        html.write("<title>"+html_title+"</title>\n")
        html.write("</head>\n")

        html.write("<body>\n")
        html.write("<div class ='table'>")
        html.write("<table class='altrowstable' id='alternatecolor'>\n")
        html.write("<caption>Diabetes Data</caption>\n")
        html.write("<thead>\n")
        html.write("<tr>\n")
        html.write("<th rowspan=" + "3" +" " + "colspan="+ "4" + ">Attributes</th>\n")
        html.write("<th rowspan=" + "1" +" " + "colspan="+ "4" + ">Class</th>\n")
        html.write("</tr>\n")
        html.write("<tr>\n")
        html.write("<th colspan=" + "2" + ">Positive</th>\n")
        html.write("<th colspan=" + "2" + ">Negative</th>\n")
        html.write("</tr>\n")
        html.write("<tr>\n")
        html.write("<th colspan=" + "1" + ">Yes</th>\n")
        html.write("<th colspan="+"1"+">No</th>\n")
        html.write("<th colspan=" + "1" + ">Yes</th>\n")
        html.write("<th colspan="+"1"+">No</th>\n")
        html.write("</tr>\n")
        html.write("</thead>\n")
        html.write("<tbody>\n")
        html.write("<tr onmouseover=" + "\"this.style.backgroundColor='#ffff66';\"" + "onmouseout=" + "\"this.style.backgroundColor='#d4e3e5';\"" + ">\n")
        html.write("<th colspan=" + "4" + ">" + header[0] + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num1) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um1) + "</th>\n")
        html.write("</tr>\n")
        html.write("<tr onmouseover=" + "\"this.style.backgroundColor='#ffff66';\"" + "onmouseout=" + "\"this.style.backgroundColor='#c3dde0';\"" + ">\n")
        html.write("<th colspan=" + "4" + ">" + header[1] + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num2) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num3) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um2) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um3) + "</th>\n")
        html.write("</tr>\n")
        html.write("<tr onmouseover=" + "\"this.style.backgroundColor='#ffff66';\"" + "onmouseout=" + "\"this.style.backgroundColor='#d4e3e5';\"" + ">\n")
        html.write("<th colspan=" + "4" + ">" + header[2] + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num4) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num5) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um4) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um5) + "</th>\n")
        html.write("</tr>\n")
        html.write("<tr onmouseover=" + "\"this.style.backgroundColor='#ffff66';\"" + "onmouseout=" + "\"this.style.backgroundColor='#c3dde0';\"" + ">\n")
        html.write("<th colspan=" + "4" + ">" + header[3] + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num6) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num7) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um6) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um7) + "</th>\n")
        html.write("</tr>\n")
        html.write("<tr onmouseover=" + "\"this.style.backgroundColor='#ffff66';\"" + "onmouseout=" + "\"this.style.backgroundColor='#d4e3e5';\"" + ">\n")
        html.write("<th colspan=" + "4" + ">" + header[4] + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num8) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num9) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um8) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um9) + "</th>\n")
        html.write("</tr>\n")
        html.write("<tr onmouseover=" + "\"this.style.backgroundColor='#ffff66';\"" + "onmouseout=" + "\"this.style.backgroundColor='#c3dde0';\"" + ">\n")
        html.write("<th colspan=" + "4" + ">" + header[5] + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num10) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num11) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um10) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um11) + "</th>\n")
        html.write("</tr>\n")
        html.write("<tr onmouseover=" + "\"this.style.backgroundColor='#ffff66';\"" + "onmouseout=" + "\"this.style.backgroundColor='#d4e3e5';\"" + ">\n")
        html.write("<th colspan=" + "4" + ">" + header[6] + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num12) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num13) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um12) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um13) + "</th>\n")
        html.write("</tr>\n")
        html.write("<tr onmouseover=" + "\"this.style.backgroundColor='#ffff66';\"" + "onmouseout=" + "\"this.style.backgroundColor='#c3dde0';\"" + ">\n")
        html.write("<th colspan=" + "4" + ">" + header[7] + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num14) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num15) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um14) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um15) + "</th>\n")
        html.write("</tr>\n")
        html.write("<tr onmouseover=" + "\"this.style.backgroundColor='#ffff66';\"" + "onmouseout=" + "\"this.style.backgroundColor='#d4e3e5';\"" + ">\n")
        html.write("<th colspan=" + "4" + ">" + header[8] + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num16) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num17) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um16) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um17) + "</th>\n")
        html.write("</tr>\n")
        html.write("<tr onmouseover=" + "\"this.style.backgroundColor='#ffff66';\"" + "onmouseout=" + "\"this.style.backgroundColor='#c3dde0';\"" + ">\n")
        html.write("<th colspan=" + "4" + ">" + header[9] + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num18) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num19) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um18) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um19) + "</th>\n")
        html.write("</tr>\n")
        html.write("<tr onmouseover=" + "\"this.style.backgroundColor='#ffff66';\"" + "onmouseout=" + "\"this.style.backgroundColor='#d4e3e5';\"" + ">\n")
        html.write("<th colspan=" + "4" + ">" + header[10] + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num20) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num21) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um20) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um21) + "</th>\n")
        html.write("</tr>\n")
        html.write("<tr onmouseover=" + "\"this.style.backgroundColor='#ffff66';\"" + "onmouseout=" + "\"this.style.backgroundColor='#c3dde0';\"" + ">\n")
        html.write("<th colspan=" + "4" + ">" + header[11] + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num22) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num23) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um22) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um23) + "</th>\n")
        html.write("</tr>\n")
        html.write("<tr onmouseover=" + "\"this.style.backgroundColor='#ffff66';\"" + "onmouseout=" + "\"this.style.backgroundColor='#d4e3e5';\"" + ">\n")
        html.write("<th colspan=" + "4" + ">" + header[12] + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num24) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num25) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um24) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um25) + "</th>\n")
        html.write("</tr>\n")
        html.write("<tr onmouseover=" + "\"this.style.backgroundColor='#ffff66';\"" + "onmouseout=" + "\"this.style.backgroundColor='#c3dde0';\"" + ">\n")
        html.write("<th colspan=" + "4" + ">" + header[13] + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num26) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(num27) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um26) + "</th>\n")
        html.write("<th colspan=" + "1" + ">" + str(um27) + "</th>\n")
        html.write("</tr>\n")
        html.write("</tbody>\n")
        html.write("</div>\n")
        html.write("</table>\n")
        if show_barchart_gender == True:
            picture(csvfile)
            html.write("<div id = 'picture'>")
            html.write("<img src = 'barchart.png'>")
            html.write("</div>")
        html.write("</body>\n")
        html.write("</html>\n")
