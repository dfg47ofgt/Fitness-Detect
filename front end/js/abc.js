function myfun(){

    // alert(ShowCount);
    // ShowCount = 5
    // ShowDate = ["2021-06-07","2021-06-04","2021-06-03","2021-06-02","2021-06-01","2021-05-19","2021-05-20"]
    // ShowSport1 = [111,123,265,154,210,156,135]
    // ShowSport2 = [142,234,215,157,231,154,251]
    // ShowSport3 = [11,6,20,21,25,23,54]


    // ShowCount = baseCount
    // ShowDate = baseDate
    // ShowSport1 = baseSport1
    // ShowSport2 = baseSport2
    // ShowSport3 = baseSport3
    baseCount = ShowCount
    baseDate = ShowDate
    baseSport1 = ShowSport1
    baseSport2 = ShowSport2
    baseSport3 = ShowSport3

    data_for_D_1 = []
    data_for_D_2 = []
    data_for_D_3 = []
    data_for_W_1 = []
    data_for_W_2 = []
    data_for_W_3 = []
    data1_for_M_1 = []
    data1_for_M_2 = []
    data1_for_M_3 = []

    today = getTodayDate()
    date_of_month = getDate()
    date_of_week =date_of_month.slice(-7,)

    for(i=0;i<30;i++){
        x = ShowDate.indexOf(date_of_month[i])
        if(x!=-1){
            // data1_for_M_1.push(ShowSport1[x]);
            // data1_for_M_2.push(ShowSport2[x]);
            // data1_for_M_3.push(ShowSport3[x]);
            data1_for_M_1.push(baseSport1[x]);
            data1_for_M_2.push(baseSport2[x]);
            data1_for_M_3.push(baseSport3[x]);

        }
        else{
            data1_for_M_1.push(0)
            data1_for_M_2.push(0)
            data1_for_M_3.push(0)
        }
    }

    data_for_W_1 = data1_for_M_1.slice(-7,)
    data_for_W_2 = data1_for_M_2.slice(-7,)
    data_for_W_3 = data1_for_M_3.slice(-7,)

    data_for_D_1 = data1_for_M_1.slice(-1)
    data_for_D_2 = data1_for_M_2.slice(-1)
    data_for_D_3 = data1_for_M_3.slice(-1)


    date_of_month = getDate2()
    date_of_week =date_of_month.slice(-7,)

    sport1 = 90
    sport2 = 65
    sport3 = 70

    //以下是要從資料庫獲取的東西，for_D是天、for_W是周、for_M是月
    //_1 _2 _3，代表三種的動作，數值就是作的次數，所以天有一筆資料，周有7，月有30


    var ctx = document.getElementById("myChart1").getContext('2d');

    var sum = [0,0,0]
    var sum_calories = 0
    for (var i = 0; i < data_for_D_1.length; i++){
        sum[0] += data_for_D_1[i]
        sum[1] += data_for_D_2[i]
        sum[2] += data_for_D_3[i]
        sum_calories += data_for_D_1[i]*sport1 + data_for_D_2[i]*sport2 + data_for_D_3[i]*sport3
        }

    Chart.defaults.font.size = 16;
    Chart.defaults.color = '#000';
    
    // 甜甜圈
    myChart1 = new Chart(ctx,{
        type: 'doughnut',
        data: {
            labels: ["深蹲", "挺舉", "臥舉"],
            datasets: [{            
                data: sum,
                backgroundColor: [
                    'rgba(255, 99, 132)',
                    'rgba(54, 162, 235)',
                    'rgba(255, 206, 86)',    
                ],
                borderWidth: 4,
                borderColor: 'rgb(255, 255, 255)',
                hoverBorderWidth: 5,
                hoverBorderColor: 'rgb(240, 240, 240)'
            }]
        },
        options:{
            responsive: true,
            maintainAspectRatio: false,
            plugins:{
                title:{
                    display: true,
                    text: '運動次數比例：',
                    position:"top",
                    align: "start",
                    font:{size:20 ,family: "Noto Sans CJK TC", weight:"normal"}
                },
                legend:{
                    display: true,
                    position: 'left',
                    labels:{
                        font:{weight:'normal',family: "Noto Sans CJK TC"},
                    }
                },
                tooltip: {
                    position:'average',
                    xAlign: "center",
                    yAlign:"bottom",
                },
            }
          
        }
    });
    var ctx2 = document.getElementById("myChart2").getContext('2d');

    Chart.defaults.color = '#000';
    
    //預設長條
    myChart2 = new Chart(ctx2, {
        type: 'bar',
        data: {
            labels: ["今日"],
            
            datasets: [{            
                label: "深蹲",
                data:data_for_D_1,
                backgroundColor:'rgba(255, 99, 132)',
                borderWidth: 1,
                borderColor: 'rgb(255, 255, 255)',
                hoverBorderWidth: 2,
                hoverBorderColor: 'rgb(240, 240, 240)'
            },{
                label: "挺舉",
                data:data_for_D_2,
                backgroundColor:'rgba(54, 162, 235)',
                borderWidth: 1,
                borderColor: 'rgb(255, 255, 255)',
                hoverBorderWidth: 2,
                hoverBorderColor: 'rgb(240, 240, 240)'
                    
            },{
                label: "臥舉",
                data:data_for_D_3,
                backgroundColor:'rgba(255, 206, 86)', 
                borderWidth: 1,
                borderColor: 'rgb(255, 255, 255)',
                hoverBorderWidth: 2,
                hoverBorderColor: 'rgb(240, 240, 240)'
            }]
        },
        options:{
            responsive: true,
            maintainAspectRatio: false,

            plugins:{
                title:{
                    display: true,
                    text: '單日運動次數：',
                    padding: 20,
                    position:"top",
                    align: "start",
                    font:{size:20 ,family: "Noto Sans CJK TC", weight:"normal"}
                },
                legend:{
                    display: false,
                    position: 'top',
                    labels:{
                        font:{weight:'normal',family:"Noto Sans CJK TC"}
                    }
                    
                }
            },
            scales:{
                x: {
                    stacked: true,
                },
                y: {
                    stacked: true
                }
            }
        }
    });
    document.getElementById("calories").innerText = '總燃燒熱量：'+ sum_calories+ " kcal"
};
////////////////////////////////////////////////////////////////////
function DayFunction(){
    myChart1.destroy();
    myChart2.destroy();
    var ctx = document.getElementById("myChart1").getContext('2d');
    
    var sum = [0,0,0]
    var sum_calories = 0
    for (var i = 0; i < data_for_D_1.length; i++){
        sum[0] += data_for_D_1[i]
        sum[1] += data_for_D_2[i]
        sum[2] += data_for_D_3[i]
        sum_calories += data_for_D_1[i]*sport1 + data_for_D_2[i]*sport2 + data_for_D_3[i]*sport3
    }

    Chart.defaults.font.size = 16;
    Chart.defaults.color = '#000';

    myChart1 = new Chart(ctx,{
        type: 'doughnut',
        data: {
            labels: ["深蹲", "挺舉", "臥舉"],
            datasets: [{            
                data: sum,
                backgroundColor: [
                    'rgba(255, 99, 132)',
                    'rgba(54, 162, 235)',
                    'rgba(255, 206, 86)',    
                ],
                borderWidth: 4,
                borderColor: 'rgb(255, 255, 255)',
                hoverBorderWidth: 5,
                hoverBorderColor: 'rgb(240, 240, 240)'
            }]
        },
        options:{
            responsive: true,
            maintainAspectRatio: false,
            plugins:{
                title:{
                    display: true,
                    text: '運動次數比例：',
                    position:"top",
                    align: "start",
                    font:{size:20 ,family: "Noto Sans CJK TC", weight:"normal"}
                },
                legend:{
                    display: true,
                    position: 'left',
                    labels:{
                        font:{weight:'normal',family: "Noto Sans CJK TC"},
                    }
                },
                tooltip: {
                    position:'average',
                    xAlign: "center",
                    yAlign:"bottom",
                },
            }
        }
    });
    var ctx2 = document.getElementById("myChart2").getContext('2d');


    Chart.defaults.color = '#000';
    
    myChart2 = new Chart(ctx2, {
        type: 'bar',
        data: {
            labels: ["今日"],
            
            datasets: [{            
                label: "深蹲",
                data:data_for_D_1,
                backgroundColor:'rgba(255, 99, 132)',
           borderWidth: 1,
                borderColor: 'rgb(255, 255, 255)',
                hoverBorderWidth: 2,
                hoverBorderColor: 'rgb(240, 240, 240)'
            },{
                label: "挺舉",
                data:data_for_D_2,
                backgroundColor:'rgba(54, 162, 235)',
           borderWidth: 1,
                borderColor: 'rgb(255, 255, 255)',
                hoverBorderWidth: 2,
                hoverBorderColor: 'rgb(240, 240, 240)'
                    
            },{
                label: "臥舉",
                data:data_for_D_3,
                backgroundColor:'rgba(255, 206, 86)', 
                borderWidth: 1,
                borderColor: 'rgb(255, 255, 255)',
                hoverBorderWidth: 2,
                hoverBorderColor: 'rgb(240, 240, 240)'
            }]
        },
        options:{
            responsive: true,
            maintainAspectRatio: false,

            plugins:{
                title:{
                    display: true,
                    text: '單日運動次數：',
                    padding: 20,
                    position:"top",
                    align: "start",
                    font:{size:20 ,family: "Noto Sans CJK TC", weight:"normal"}
                },
                legend:{
                    display: false,
                    position: 'top',
                    labels:{
                        font:{weight:'bold'}
                    }
                    
                }
            },
            scales:{
                x: {
                    stacked: true,
                },
                y: {
                    stacked: true
                }
            }
        }
    });
    document.getElementById("calories").innerText = '單日總燃燒熱量：'+ sum_calories+ " kcal"
};

////////////////////////////////////////////////////////////////////
function WeekFunction(){
    myChart1.destroy();
    myChart2.destroy();
    var ctx = document.getElementById("myChart1").getContext('2d');

    var sum = [0,0,0]
    var sum_calories = 0
    for (var i = 0; i < data_for_W_1.length; i++){
        sum[0] += data_for_W_1[i]
        sum[1] += data_for_W_2[i]
        sum[2] += data_for_W_3[i]
        sum_calories += data_for_W_1[i]*sport1 + data_for_W_2[i]*sport2 + data_for_W_3[i]*sport3
    }
    
    
    //Chart.defaults.font.Family ='Arial';
    Chart.defaults.font.size = 16;
    Chart.defaults.color = '#000';

    myChart1 = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ["深蹲", "挺舉", "臥舉"],
            datasets: [{            
                data: sum,
                backgroundColor: [
                    'rgba(255, 99, 132)',
                    'rgba(54, 162, 235)',
                    'rgba(255, 206, 86)',    
                ],
                borderWidth: 4,
                borderColor: 'rgb(255, 255, 255)',
                hoverBorderWidth: 5,
                hoverBorderColor: 'rgb(240, 240, 240)'
            }]
        },
        options:{
            responsive: true,
            maintainAspectRatio: false,
            plugins:{
                title:{
                    display: true,
                    text: '運動次數比例：',
                    position:"top",
                    align: "start",
                    font:{size:20 ,family: "Noto Sans CJK TC", weight:"normal"}
                },
                legend:{
                    display: true,
                    position: 'left',
                    labels:{
                        font:{weight:'normal',family: "Noto Sans CJK TC"},
                    }
                },
                tooltip: {
                    position:'average',
                    xAlign: "center",
                    yAlign:"bottom",
                },
            }
        }
    });

    var ctx2 = document.getElementById("myChart2").getContext('2d');

    Chart.defaults.color = '#000';
    myChart2 = new Chart(ctx2, {
        type: 'bar',
        data: {
            labels: date_of_week,
            
            datasets: [{            
                label: "深蹲",
                data:data_for_W_1,
                backgroundColor:'rgba(255, 99, 132)',
                borderWidth: 1,
                borderColor: 'rgb(255, 255, 255)',
                hoverBorderWidth: 2,
                hoverBorderColor: 'rgb(240, 240, 240)'
            },{
                label: "挺舉",
                data:data_for_W_2,
                backgroundColor:'rgba(54, 162, 235)',
                borderWidth: 1,
                borderColor: 'rgb(255, 255, 255)',
                hoverBorderWidth: 2,
                hoverBorderColor: 'rgb(240, 240, 240)'
                    
            },{
                label: "臥舉",
                data:data_for_W_3,
                backgroundColor:'rgba(255, 206, 86)', 
                borderWidth: 1,
                borderColor: 'rgb(255, 255, 255)',
                hoverBorderWidth: 2,
                hoverBorderColor: 'rgb(240, 240, 240)'
            }]
        },
        options:{
            responsive: true,
            maintainAspectRatio: false,

            plugins:{
                title:{
                    display: true,
                    text: '週運動次數：',
                    padding: 20,
                    position:"top",
                    align: "start",
                    font:{size:20 ,family: "Noto Sans CJK TC", weight:"normal"}
                },
                legend:{
                    display: false,
                    position: 'top',
                    labels:{
                        font:{weight:'bold'}
                    }
                    
                }
            },
            scales:{
                x: {
                    stacked: true,
                },
                y: {
                    stacked: true
                }
            }
        }
    });
    document.getElementById("calories").innerText = '單週總燃燒熱量：'+ sum_calories+ " kcal"
};
////////////////////////////////////////////////////////////////////
function MonthFunction(){
    myChart1.destroy();
    myChart2.destroy();
    var ctx = document.getElementById("myChart1").getContext('2d');

    var sum = [0,0,0]
    var sum_calories = 0
    for (var i = 0; i < data1_for_M_1.length; i++){
        sum[0] += data1_for_M_1[i]
        sum[1] += data1_for_M_2[i]
        sum[2] += data1_for_M_3[i]
        sum_calories += data1_for_M_1[i]*sport1 + data1_for_M_2[i]*sport2 + data1_for_M_3[i]*sport3
    }


    //Chart.defaults.font.Family ='Arial';
    Chart.defaults.font.size = 16;
    Chart.defaults.color = '#000';

    myChart1 = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ["深蹲", "挺舉", "臥舉"],
            datasets: [{            
                data: sum,
                backgroundColor: [
                    'rgba(249, 97, 103)',
                    'rgba(54, 162, 235)',
                    'rgba(255, 206, 86)',    
                ],
          borderWidth: 4,
                borderColor: 'rgb(255, 255, 255)',
                hoverBorderWidth: 5,
                hoverBorderColor: 'rgb(240, 240, 240)'
            }]
        },
        options:{
            responsive: true,
            maintainAspectRatio: false,
            plugins:{
                title:{
                    display: true,
                    text: '運動次數比例：',
                    position:"top",
                    align: "start",
                    font:{size:20 ,family: "Noto Sans CJK TC", weight:"normal"}
                },
                legend:{
                    display: true,
                    position: 'left',
                    labels:{
                        font:{weight:'normal',family: "Noto Sans CJK TC"},
                    }
                },
                tooltip: {
                    position:'average',
                    xAlign: "center",
                    yAlign:"bottom",
                },
            }
        }
    });

    var ctx2 = document.getElementById("myChart2").getContext('2d');
    Chart.defaults.color = '#000';
    myChart2 = new Chart(ctx2, {
        type: 'bar',
        data: {
            labels: date_of_month,
            
            datasets: [{            
                label: "深蹲",
                data:data1_for_M_1,
                backgroundColor:'rgba(255, 99, 132)',
           borderWidth: 1,
                borderColor: 'rgb(255, 255, 255)',
                hoverBorderWidth: 2,
                hoverBorderColor: 'rgb(240, 240, 240)'
            },{
                label: "挺舉",
                data:data1_for_M_2,
                backgroundColor:'rgba(54, 162, 235)',
           borderWidth: 1,
                borderColor: 'rgb(255, 255, 255)',
                hoverBorderWidth: 2,
                hoverBorderColor: 'rgb(240, 240, 240)'
                    
            },{
                label: "臥舉",
                data:data1_for_M_3,
                backgroundColor:'rgba(255, 206, 86)', 
          borderWidth: 1,
                borderColor: 'rgb(255, 255, 255)',
                hoverBorderWidth: 2,
                hoverBorderColor: 'rgb(240, 240, 240)'
            }]
        },
        options:{
            responsive: true,
            maintainAspectRatio: false,

            plugins:{
                title:{
                    display: true,
                    text: '月運動次數：',
                    padding: 20,
                    position:"top",
                    align: "start",
                    font:{size:20 ,family: "Noto Sans CJK TC", weight:"normal"}
                },
                legend:{
                    display: false,
                    position: 'top',
                    labels:{
                        font:{weight:'bold'}
                    }
                    
                }
            },
            scales:{
                x: {
                    stacked: true,
                },
                y: {
                    stacked: true
                }
            }
        }
    });
    document.getElementById("calories").innerText = '單月燃燒熱量： '+ sum_calories
};


function getTodayDate() {
    var fullDate = new Date();
    var yyyy = fullDate.getFullYear();
    var MM = (fullDate.getMonth() + 1) >= 10 ? (fullDate.getMonth() + 1) : ("0" + (fullDate.getMonth() + 1));
    var dd = fullDate.getDate() < 10 ? ("0"+fullDate.getDate()) : fullDate.getDate();
    var today = yyyy + "-" + MM + "-" + dd;
    return today;
};


function getDate() {
    var date_of_month =[]
    for(i=29;i>=0;i--){
        var fullDate = new Date(new Date().getTime() - 24 * 60 * 60 * 1000*i);
        var yyyy = fullDate.getFullYear();
        var MM = (fullDate.getMonth() + 1) >= 10 ? (fullDate.getMonth() + 1) : ("0" + (fullDate.getMonth() + 1));
        var dd = fullDate.getDate() < 10 ? ("0"+fullDate.getDate()) : fullDate.getDate();
        var date = yyyy + "-" + MM + "-" + dd;
        date_of_month.push(date)

    }
    return date_of_month
};


function getDate2() {
    var date_of_month =[]
    for(i=29;i>=0;i--){
        var fullDate = new Date(new Date().getTime() - 24 * 60 * 60 * 1000*i);
       y�H��͌R\F�@���_˴�   `l�   `  qE�3��}   �(  �� �   �   �   �S �`       L`       S0�`    (    L`       0Rc    
       ¹                a`    �� I`    ����Da    
       �  S5IaD  �         Qbv�«   fileUriToPath   
 �@� dQw���г   G:\Eclipse_IDE\eclipse-jee-2020-12\eclipse\plugin