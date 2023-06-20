<<<<<<< HEAD
function myfun(){
    data_for_D_1 = []
    data_for_D_2 = []
    data_for_D_3 = []
	data_for_D_4 = []

    data_for_W_1 = []
    data_for_W_2 = []
    data_for_W_3 = []
	data_for_W_4 = []

    data1_for_M_1 = []
    data1_for_M_2 = []
    data1_for_M_3 = []
	data1_for_M_4 = []


    today = getTodayDate()
    date_of_month = getDate()
    date_of_week =date_of_month.slice(-7,)

    for(i=0;i<30;i++){
        x = ShowDate.indexOf(date_of_month[i])
        if(x!=-1){
            data1_for_M_1.push(ShowSport1[x]);
            data1_for_M_2.push(ShowSport2[x]);
            data1_for_M_3.push(ShowSport3[x]);
			data1_for_M_4.push(ShowSport4[x]);

			// var pointNum = parseInt(ShowSport1[x]);
        }
        else{
            data1_for_M_1.push(0)
            data1_for_M_2.push(0)
            data1_for_M_3.push(0)
			data1_for_M_4.push(0)

        }
    }
		// alert(typeof(pointNum));

    data_for_W_1 = data1_for_M_1.slice(-7,)
    data_for_W_2 = data1_for_M_2.slice(-7,)
    data_for_W_3 = data1_for_M_3.slice(-7,)
	data_for_W_4 = data1_for_M_4.slice(-7,)

    data_for_D_1 = data1_for_M_1.slice(-1)
    data_for_D_2 = data1_for_M_2.slice(-1)
    data_for_D_3 = data1_for_M_3.slice(-1)
    data_for_D_4 = data1_for_M_4.slice(-1)


    date_of_month = getDate2()
    date_of_week =date_of_month.slice(-7,)
    //順序: 舉啞鈴、深蹲、伏地挺身、跑步
    sport1 = 90
    sport2 = 65
    sport3 = 70
	sport4 = 30


    //以下是要從資料庫獲取的東西，for_D是天、for_W是周、for_M是月
    //_1 _2 _3，代表三種的動作，數值就是作的次數，所以天有一筆資料，周有7，月有30


    var ctx = document.getElementById("myChart1").getContext('2d');

    var sum = [0,0,0]
    var sum_calories = 0
    for (var i = 0; i < data_for_D_1.length; i++){
        sum[0] += data_for_D_1[i]*1
        sum[1] += data_for_D_2[i]*1
        sum[2] += data_for_D_3[i]*1
		
        sum_calories += data_for_D_1[i]*sport1 + data_for_D_2[i]*sport2 + data_for_D_3[i]*sport3 + data_for_D_4[i]*sport4
        }
    sum_kcal = Math.ceil(sum_calories/1000);
    Chart.defaults.font.size = 16;
    Chart.defaults.color = '#000';
    
    // 甜甜圈
    myChart1 = new Chart(ctx,{
        type: 'doughnut',
        data: {
            labels: ["舉啞鈴", "深蹲", "伏地挺身"],
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
                label: "舉啞鈴",
                data:data_for_D_1,
                backgroundColor:'rgba(255, 99, 132)',
                borderWidth: 1,
                borderColor: 'rgb(255, 255, 255)',
                hoverBorderWidth: 2,
                hoverBorderColor: 'rgb(240, 240, 240)'
            },{
                label: "深蹲",
                data:data_for_D_2,
                backgroundColor:'rgba(54, 162, 235)',
                borderWidth: 1,
                borderColor: 'rgb(255, 255, 255)',
                hoverBorderWidth: 2,
                hoverBorderColor: 'rgb(240, 240, 240)'
                    
            },{
                label: "伏地挺身",
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
                    text: '今日運動次數：',
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
    document.getElementById("calories").innerText = '今日總燃燒熱量：'+ sum_kcal+ " kcal"
	};
	////////////////////////////////////////////////////////////////////
	function DayFunction(){
		myChart1.destroy();
		myChart2.destroy();
		var ctx = document.getElementById("myChart1").getContext('2d');
		
		var sum = [0,0,0]
		var sum_calories = 0
		for (var i = 0; i < data_for_D_1.length; i++){
			sum[0] += data_for_D_1[i]*1
			sum[1] += data_for_D_2[i]*1
			sum[2] += data_for_D_3[i]*1
			sum_calories += data_for_D_1[i]*sport1 + data_for_D_2[i]*sport2 + data_for_D_3[i]*sport3 + data_for_D_4[i]*sport4
		}
		sum_kcal = Math.ceil(sum_calories/1000);
		Chart.defaults.font.size = 16;
		Chart.defaults.color = '#000';
		
		myChart1 = new Chart(ctx,{
			type: 'doughnut',
			data: {
				labels: ["舉啞鈴", "深蹲", "伏地挺身"],
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
					label: "舉啞鈴",
					data:data_for_D_1,
					backgroundColor:'rgba(255, 99, 132)',
			borderWidth: 1,
					borderColor: 'rgb(255, 255, 255)',
					hoverBorderWidth: 2,
					hoverBorderColor: 'rgb(240, 240, 240)'
				},{
					label: "深蹲",
					data:data_for_D_2,
					backgroundColor:'rgba(54, 162, 235)',
			borderWidth: 1,
					borderColor: 'rgb(255, 255, 255)',
					hoverBorderWidth: 2,
					hoverBorderColor: 'rgb(240, 240, 240)'
						
				},{
					label: "伏地挺身",
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
						text: '今日運動次數：',
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
		document.getElementById("calories").innerText = '今日總燃燒熱量：'+ sum_kcal+ " kcal"
	};

	////////////////////////////////////////////////////////////////////
	function WeekFunction(){
		myChart1.destroy();
		myChart2.destroy();
		var ctx = document.getElementById("myChart1").getContext('2d');

		var sum = [0,0,0]
		var sum_calories = 0
		for (var i = 0; i < data_for_W_1.length; i++){
			sum[0] += data_for_W_1[i]*1
			sum[1] += data_for_W_2[i]*1
			sum[2] += data_for_W_3[i]*1
			sum_calories += data_for_W_1[i]*sport1 + data_for_W_2[i]*sport2 + data_for_W_3[i]*sport3 + data_for_W_4[i]*sport4
		}
		sum_kcal = Math.ceil(sum_calories/1000);
		
		//Chart.defaults.font.Family ='Arial';
		Chart.defaults.font.size = 16;
		Chart.defaults.color = '#000';

		myChart1 = new Chart(ctx, {
			type: 'doughnut',
			data: {
				labels: ["舉啞鈴", "深蹲", "伏地挺身"],
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
					label: "舉啞鈴",
					data:data_for_W_1,
					backgroundColor:'rgba(255, 99, 132)',
					borderWidth: 1,
					borderColor: 'rgb(255, 255, 255)',
					hoverBorderWidth: 2,
					hoverBorderColor: 'rgb(240, 240, 240)'
				},{
					label: "深蹲",
					data:data_for_W_2,
					backgroundColor:'rgba(54, 162, 235)',
					borderWidth: 1,
					borderColor: 'rgb(255, 255, 255)',
					hoverBorderWidth: 2,
					hoverBorderColor: 'rgb(240, 240, 240)'
						
				},{
					label: "伏地挺身",
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
						text: '前7天運動次數：',
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
		document.getElementById("calories").innerText = '前七日總燃燒熱量：'+ sum_kcal+ " kcal"
	};
	////////////////////////////////////////////////////////////////////
	function MonthFunction(){
		myChart1.destroy();
		myChart2.destroy();
		var ctx = document.getElementById("myChart1").getContext('2d');

		var sum = [0,0,0]
		var sum_calories = 0
		for (var i = 0; i < data1_for_M_1.length; i++){
			sum[0] += data1_for_M_1[i]*1
			sum[1] += data1_for_M_2[i]*1
			sum[2] += data1_for_M_3[i]*1
			sum_calories += data1_for_M_1[i]*sport1 + data1_for_M_2[i]*sport2 + data1_for_M_3[i]*sport3 + data1_for_M_4[i]*sport4
		}
		sum_kcal = Math.ceil(sum_calories/1000);

		//Chart.defaults.font.Family ='Arial';
		Chart.defaults.font.size = 16;
		Chart.defaults.color = '#000';

		myChart1 = new Chart(ctx, {
			type: 'doughnut',
			data: {
				labels: ["舉啞鈴", "深蹲", "伏地挺身"],
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
					label: "舉啞鈴",
					data:data1_for_M_1,
					backgroundColor:'rgba(255, 99, 132)',
			borderWidth: 1,
					borderColor: 'rgb(255, 255, 255)',
					hoverBorderWidth: 2,
					hoverBorderColor: 'rgb(240, 240, 240)'
				},{
					label: "深蹲",
					data:data1_for_M_2,
					backgroundColor:'rgba(54, 162, 235)',
			borderWidth: 1,
					borderColor: 'rgb(255, 255, 255)',
					hoverBorderWidth: 2,
					hoverBorderColor: 'rgb(240, 240, 240)'
						
				},{
					label: "伏地挺身",
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
						text: '前30天運動次數：',
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
		document.getElementById("calories").innerText = '前三十日燃燒熱量： '+ sum_kcal+ " kcal"
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
			var MM = (fullDate.getMonth() + 1) >= 10 ? (fullDate.getMonth() + 1) : ("0" + (fullDate.getMonth() + 1));
			var dd = fullDate.getDate() < 10 ? ("0"+fullDate.getDate()) : fullDate.getDate();
			var date = MM + "/" + dd;
			date_of_month.push(date)

		}
		return date_of_month
	};
=======
function myfun(){
    data_for_D_1 = []
    data_for_D_2 = []
    data_for_D_3 = []
	data_for_D_4 = []

    data_for_W_1 = []
    data_for_W_2 = []
    data_for_W_3 = []
	data_for_W_4 = []

    data1_for_M_1 = []
    data1_for_M_2 = []
    data1_for_M_3 = []
	data1_for_M_4 = []


    today = getTodayDate()
    date_of_month = getDate()
    date_of_week =date_of_month.slice(-7,)

    for(i=0;i<30;i++){
        x = ShowDate.indexOf(date_of_month[i])
        if(x!=-1){
            data1_for_M_1.push(ShowSport1[x]);
            data1_for_M_2.push(ShowSport2[x]);
            data1_for_M_3.push(ShowSport3[x]);
			data1_for_M_4.push(ShowSport4[x]);

			// var pointNum = parseInt(ShowSport1[x]);
        }
        else{
            data1_for_M_1.push(0)
            data1_for_M_2.push(0)
            data1_for_M_3.push(0)
			data1_for_M_4.push(0)

        }
    }
		// alert(typeof(pointNum));

    data_for_W_1 = data1_for_M_1.slice(-7,)
    data_for_W_2 = data1_for_M_2.slice(-7,)
    data_for_W_3 = data1_for_M_3.slice(-7,)
	data_for_W_4 = data1_for_M_4.slice(-7,)

    data_for_D_1 = data1_for_M_1.slice(-1)
    data_for_D_2 = data1_for_M_2.slice(-1)
    data_for_D_3 = data1_for_M_3.slice(-1)
    data_for_D_4 = data1_for_M_4.slice(-1)


    date_of_month = getDate2()
    date_of_week =date_of_month.slice(-7,)
    //順序: 舉啞鈴、深蹲、伏地挺身、跑步
    sport1 = 90
    sport2 = 65
    sport3 = 70
	sport4 = 30


    //以下是要從資料庫獲取的東西，for_D是天、for_W是周、for_M是月
    //_1 _2 _3，代表三種的動作，數值就是作的次數，所以天有一筆資料，周有7，月有30


    var ctx = document.getElementById("myChart1").getContext('2d');

    var sum = [0,0,0]
    var sum_calories = 0
    for (var i = 0; i < data_for_D_1.length; i++){
        sum[0] += data_for_D_1[i]*1
        sum[1] += data_for_D_2[i]*1
        sum[2] += data_for_D_3[i]*1
		
        sum_calories += data_for_D_1[i]*sport1 + data_for_D_2[i]*sport2 + data_for_D_3[i]*sport3 + data_for_D_4[i]*sport4
        }
    sum_kcal = Math.ceil(sum_calories/1000);
    Chart.defaults.font.size = 16;
    Chart.defaults.color = '#000';
    
    // 甜甜圈
    myChart1 = new Chart(ctx,{
        type: 'doughnut',
        data: {
            labels: ["舉啞鈴", "深蹲", "伏地挺身"],
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
                label: "舉啞鈴",
                data:data_for_D_1,
                backgroundColor:'rgba(255, 99, 132)',
                borderWidth: 1,
                borderColor: 'rgb(255, 255, 255)',
                hoverBorderWidth: 2,
                hoverBorderColor: 'rgb(240, 240, 240)'
            },{
                label: "深蹲",
                data:data_for_D_2,
                backgroundColor:'rgba(54, 162, 235)',
                borderWidth: 1,
                borderColor: 'rgb(255, 255, 255)',
                hoverBorderWidth: 2,
                hoverBorderColor: 'rgb(240, 240, 240)'
                    
            },{
                label: "伏地挺身",
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
                    text: '今日運動次數：',
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
    document.getElementById("calories").innerText = '今日總燃燒熱量：'+ sum_kcal+ " kcal"
	};
	////////////////////////////////////////////////////////////////////
	function DayFunction(){
		myChart1.destroy();
		myChart2.destroy();
		var ctx = document.getElementById("myChart1").getContext('2d');
		
		var sum = [0,0,0]
		var sum_calories = 0
		for (var i = 0; i < data_for_D_1.length; i++){
			sum[0] += data_for_D_1[i]*1
			sum[1] += data_for_D_2[i]*1
			sum[2] += data_for_D_3[i]*1
			sum_calories += data_for_D_1[i]*sport1 + data_for_D_2[i]*sport2 + data_for_D_3[i]*sport3 + data_for_D_4[i]*sport4
		}
		sum_kcal = Math.ceil(sum_calories/1000);
		Chart.defaults.font.size = 16;
		Chart.defaults.color = '#000';
		
		myChart1 = new Chart(ctx,{
			type: 'doughnut',
			data: {
				labels: ["舉啞鈴", "深蹲", "伏地挺身"],
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
					label: "舉啞鈴",
					data:data_for_D_1,
					backgroundColor:'rgba(255, 99, 132)',
			borderWidth: 1,
					borderColor: 'rgb(255, 255, 255)',
					hoverBorderWidth: 2,
					hoverBorderColor: 'rgb(240, 240, 240)'
				},{
					label: "深蹲",
					data:data_for_D_2,
					backgroundColor:'rgba(54, 162, 235)',
			borderWidth: 1,
					borderColor: 'rgb(255, 255, 255)',
					hoverBorderWidth: 2,
					hoverBorderColor: 'rgb(240, 240, 240)'
						
				},{
					label: "伏地挺身",
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
						text: '今日運動次數：',
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
		document.getElementById("calories").innerText = '今日總燃燒熱量：'+ sum_kcal+ " kcal"
	};

	////////////////////////////////////////////////////////////////////
	function WeekFunction(){
		myChart1.destroy();
		myChart2.destroy();
		var ctx = document.getElementById("myChart1").getContext('2d');

		var sum = [0,0,0]
		var sum_calories = 0
		for (var i = 0; i < data_for_W_1.length; i++){
			sum[0] += data_for_W_1[i]*1
			sum[1] += data_for_W_2[i]*1
			sum[2] += data_for_W_3[i]*1
			sum_calories += data_for_W_1[i]*sport1 + data_for_W_2[i]*sport2 + data_for_W_3[i]*sport3 + data_for_W_4[i]*sport4
		}
		sum_kcal = Math.ceil(sum_calories/1000);
		
		//Chart.defaults.font.Family ='Arial';
		Chart.defaults.font.size = 16;
		Chart.defaults.color = '#000';

		myChart1 = new Chart(ctx, {
			type: 'doughnut',
			data: {
				labels: ["舉啞鈴", "深蹲", "伏地挺身"],
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
					label: "舉啞鈴",
					data:data_for_W_1,
					backgroundColor:'rgba(255, 99, 132)',
					borderWidth: 1,
					borderColor: 'rgb(255, 255, 255)',
					hoverBorderWidth: 2,
					hoverBorderColor: 'rgb(240, 240, 240)'
				},{
					label: "深蹲",
					data:data_for_W_2,
					backgroundColor:'rgba(54, 162, 235)',
					borderWidth: 1,
					borderColor: 'rgb(255, 255, 255)',
					hoverBorderWidth: 2,
					hoverBorderColor: 'rgb(240, 240, 240)'
						
				},{
					label: "伏地挺身",
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
						text: '前7天運動次數：',
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
		document.getElementById("calories").innerText = '前七日總燃燒熱量：'+ sum_kcal+ " kcal"
	};
	////////////////////////////////////////////////////////////////////
	function MonthFunction(){
		myChart1.destroy();
		myChart2.destroy();
		var ctx = document.getElementById("myChart1").getContext('2d');

		var sum = [0,0,0]
		var sum_calories = 0
		for (var i = 0; i < data1_for_M_1.length; i++){
			sum[0] += data1_for_M_1[i]*1
			sum[1] += data1_for_M_2[i]*1
			sum[2] += data1_for_M_3[i]*1
			sum_calories += data1_for_M_1[i]*sport1 + data1_for_M_2[i]*sport2 + data1_for_M_3[i]*sport3 + data1_for_M_4[i]*sport4
		}
		sum_kcal = Math.ceil(sum_calories/1000);

		//Chart.defaults.font.Family ='Arial';
		Chart.defaults.font.size = 16;
		Chart.defaults.color = '#000';

		myChart1 = new Chart(ctx, {
			type: 'doughnut',
			data: {
				labels: ["舉啞鈴", "深蹲", "伏地挺身"],
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
					label: "舉啞鈴",
					data:data1_for_M_1,
					backgroundColor:'rgba(255, 99, 132)',
			borderWidth: 1,
					borderColor: 'rgb(255, 255, 255)',
					hoverBorderWidth: 2,
					hoverBorderColor: 'rgb(240, 240, 240)'
				},{
					label: "深蹲",
					data:data1_for_M_2,
					backgroundColor:'rgba(54, 162, 235)',
			borderWidth: 1,
					borderColor: 'rgb(255, 255, 255)',
					hoverBorderWidth: 2,
					hoverBorderColor: 'rgb(240, 240, 240)'
						
				},{
					label: "伏地挺身",
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
						text: '前30天運動次數：',
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
		document.getElementById("calories").innerText = '前三十日燃燒熱量： '+ sum_kcal+ " kcal"
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
			var MM = (fullDate.getMonth() + 1) >= 10 ? (fullDate.getMonth() + 1) : ("0" + (fullDate.getMonth() + 1));
			var dd = fullDate.getDate() < 10 ? ("0"+fullDate.getDate()) : fullDate.getDate();
			var date = MM + "/" + dd;
			date_of_month.push(date)

		}
		return date_of_month
	};
>>>>>>> origin/main
window.onload = myfun;