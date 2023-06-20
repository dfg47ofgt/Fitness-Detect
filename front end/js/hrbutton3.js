!function() {

  var today = moment();

  function Calendar(selector, events) {
    this.el = document.querySelector(selector);
    this.events = events;
    this.current = moment().date(1);
    this.draw();
    var current = document.querySelector('.today');
    if(current) {
      var self = this;
      window.setTimeout(function() {
        self.openDay(current);
      }, 500);
    }
  }


  Calendar.prototype.draw = function() {
    //Create Header
    this.drawHeader();

    //Draw Month
    this.drawMonth();
  }

  Calendar.prototype.drawHeader = function() {
    var self = this;
    if(!this.header) {
      //Create the header elements
      this.header = createElement('div', 'header');
      this.header.className = 'header';

      this.title = createElement('h1');

      var right = createElement('div', 'right');
      right.addEventListener('click', function() { self.nextMonth(); });

      var left = createElement('div', 'left');
      left.addEventListener('click', function() { self.prevMonth(); });

      //Append the Elements

      this.header.appendChild(this.title); 
      this.header.appendChild(right);
      this.header.appendChild(left);
      this.el.appendChild(this.header);
    }

    this.title.innerHTML = this.current.format('MMMM YYYY');
  }

  //不隨機分配
  Calendar.prototype.drawMonth = function() {
    var self = this;
    
    this.events.forEach(function(ev) {
      ev.date =moment(ev.date);
    });
    
    if(this.month) {
      this.oldMonth = this.month;
      this.oldMonth.className = 'month out ' + (self.next ? 'next' : 'prev');
      this.oldMonth.addEventListener('webkitAnimationEnd', function() {
        self.oldMonth.parentNode.removeChild(self.oldMonth);
        self.month = createElement('div', 'month');
        self.backFill();
        self.currentMonth();
        self.fowardFill();
        self.el.appendChild(self.month);
        window.setTimeout(function() {
          self.month.className = 'month in ' + (self.next ? 'next' : 'prev');
        }, 16);
      });
    } else {
        this.month = createElement('div', 'month');
        this.el.appendChild(this.month);
        this.backFill();
        this.currentMonth();
        this.fowardFill();
        this.month.className = 'month new';
    }
  } 

  //調整灰色日期
  Calendar.prototype.backFill = function() {
    var clone = this.current.clone();
    var dayOfWeek = clone.day();

    if(!dayOfWeek) { return; }

    clone.subtract('days', dayOfWeek+1);

    for(var i = dayOfWeek; i > 0 ; i--) {
      this.drawDay(clone.add('days', 1));
    }
  }

  Calendar.prototype.fowardFill = function() {
    var clone = this.current.clone().add('months', 1).subtract('days', 1);
    var dayOfWeek = clone.day();

    if(dayOfWeek === 6) { return; }

    for(var i = dayOfWeek; i < 0;  i++) {
      this.drawDay(clone.add('day', 1));
    }
  }

  Calendar.prototype.currentMonth = function() {
    var clone = this.current.clone();
    while(clone.month() === this.current.month()) {
      this.drawDay(clone);
      clone.add('days', 1);
    }
  }
  //var a =1;
  Calendar.prototype.getWeek = function(day) {
    if(!this.week || day.day() === 0) {
      // alert("!!!");
      this.week = createElement('div', 'week');
      this.month.appendChild(this.week);
    }
    // this.weekbtm = createElement('div', 'weekbtm');
    // this.month.appendChild(this.weekbtm);
  }

  Calendar.prototype.drawDay = function(day) {
    var self = this;
    this.getWeek(day);
    
    //Outer Day
    var outer = createElement('div', this.getDayClass(day));
    outer.addEventListener('click', function() {
      self.openDay(this);
    });

    //Day Name
    var name = createElement('div', 'day-name', day.format('ddd'));

    //Day Number
    var number = createElement('div', 'day-number', day.format('DD'));


    //Events
    var events = createElement('div', 'day-events');
    this.drawEvents(day, events);

    outer.appendChild(name);
    outer.appendChild(number);
    outer.appendChild(events);
    this.week.appendChild(outer);
  }

  Calendar.prototype.drawEvents = function(day, element) {
    if(day.month() === this.current.month()) {
      var todaysEvents = this.events.reduce(function(memo, ev) {
        if(ev.date.isSame(day, 'day')) {
          memo.push(ev);
        }
        return memo;
      }, []);

      todaysEvents.forEach(function(ev) {
        var evSpan = createElement('span', ev.color);
        element.appendChild(evSpan);
      });
    }

  }

  Calendar.prototype.getDayClass = function(day) {
    classes = ['day'];
    if(day.month() !== this.current.month()) {
      classes.push('other');
    } else if (today.isSame(day, 'day')) {
      classes.push('today');
    }
    return classes.join(' ');
  }

  Calendar.prototype.openDay = function(el) {
    var details, arrow;
    var dayNumber = +el.querySelectorAll('.day-number')[0].innerText || +el.querySelectorAll('.day-number')[0].textContent;
    var day = this.current.clone().date(dayNumber);
    var enoch = (moment(day).format('YYYY-MM-DD'));
    

    var currentOpened = document.querySelector('.details');

    //Check to see if there is an open detais box on the current row
    if(currentOpened && currentOpened.parentNode === el.parentNode) {
      details = currentOpened;
      arrow = document.querySelector('.arrow');
    } else {
      //Close the open events on differnt week row
      //currentOpened && currentOpened.parentNode.removeChild(currentOpened);
      if(currentOpened) {
        currentOpened.addEventListener('webkitAnimationEnd', function() {
          currentOpened.parentNode.removeChild(currentOpened);
        });
        currentOpened.addEventListener('oanimationend', function() {
          currentOpened.parentNode.removeChild(currentOpened);
        });
        currentOpened.addEventListener('msAnimationEnd', function() {
          currentOpened.parentNode.removeChild(currentOpened);
        });
        currentOpened.addEventListener('animationend', function() {
          currentOpened.parentNode.removeChild(currentOpened);
        });
        currentOpened.className = 'details out';
      }

      //Create the Details Container
      details = createElement('div', 'details in');

      //Create the arrow
      var arrow = createElement('div', 'arrow');

      //Create the event wrapper

      details.appendChild(arrow);
      el.parentNode.appendChild(details);
    }

    var todaysEvents = this.events.reduce(function(memo, ev) {
      if(ev.date.isSame(day, 'day')) {
        memo.push(ev);
      }
      return memo;
    }, []);

    this.renderEvents(todaysEvents, details, enoch);

    arrow.style.left = el.offsetLeft - el.parentNode.offsetLeft + 27 + 'px';
  }

  Calendar.prototype.renderEvents = function(events, ele, enoch) {
    //Remove any events in the current details element
    //alert(enoch)
    var currentWrapper = ele.querySelector('.events');
    var wrapper = createElement('div', 'events in' + (currentWrapper ? ' new' : ''));

    events.forEach(function(ev) {
      var div = createElement('div', 'event');
      var square = createElement('div', 'event-category ' + ev.color);
      var span = createElement('span', '', ev.eventName);
      // 應該是寫在這邊 但不知道咬怎麼寫
      
      div.appendChild(square);
      div.appendChild(span);
      wrapper.appendChild(div);
      
    })

    if(!events.length) {
      var div = createElement('div', 'event empty');
      var span = createElement('span', '', '這天沒有運動喔！');

      div.appendChild(span);
      wrapper.appendChild(div);
    }
    else{
      var div = createElement('div', 'videoBtn');
      div.setAttribute('id', 'confirm');
      var link_video = document.createElement('span');
      var linkText = document.createTextNode("觀看當日運動影片");

      link_video.appendChild(linkText);
      div.appendChild(link_video);
      wrapper.appendChild(div);

      div.addEventListener('click', function() {
				cuteAlert({
					view:"watchout",
					type: "success",
					title: "你按下去了",
					message: "可是我還是不知道咬怎麼改變大小",
					buttonText: "確定",
					date: enoch, //這裡改成要抓的檔案名稱（格式為YYYY-MM-DD）
				})

      });
    }

    if(currentWrapper) {
      currentWrapper.className = 'events out';
      currentWrapper.addEventListener('webkitAnimationEnd', function() {
        currentWrapper.parentNode.removeChild(currentWrapper);
        ele.appendChild(wrapper);
      });
      currentWrapper.addEventListener('oanimationend', function() {
        currentWrapper.parentNode.removeChild(currentWrapper);
        ele.appendChild(wrapper);
      });
      currentWrapper.addEventListener('msAnimationEnd', function() {
        currentWrapper.parentNode.removeChild(currentWrapper);
        ele.appendChild(wrapper);
      });
      currentWrapper.addEventListener('animationend', function() {
        currentWrapper.parentNode.removeChild(currentWrapper);
        ele.appendChild(wrapper);
      });
    } else {
      ele.appendChild(wrapper);
    }
  }

  //箭頭
  Calendar.prototype.nextMonth = function() {
    this.current.add('months', 1);
    this.next = true;
    this.draw();
  }

  Calendar.prototype.prevMonth = function() {
    this.current.subtract('months', 1);
    this.next = false;
    this.draw();
  }


  window.Calendar = Calendar;

  function createElement(tagName, className, innerText) {
    var ele = document.createElement(tagName);
    if(className) {
      ele.className = className;
    }
    if(innerText) {
      ele.innderText = ele.textContent = innerText;
    }
    return ele;
  }
}()

// //新增活動
// !function() {
//   var data = [
//     { eventName: '做了n下深蹲', color: 'orange' ,date:'2021-08-01' },
//     { eventName: '做了n下挺舉',  color: 'blue' ,date:'2021-08-01'},
//     { eventName: '做了n下臥舉', color: 'green',date:'2021-08-01' },
//     { eventName: '做了12下深蹲', color: 'orange' ,date:'2021-08-05' },
//     { eventName: '做了30下挺舉',  color: 'blue' ,date:'2021-08-05'},
//     { eventName: '做了35下臥舉', color: 'green',date:'2021-08-05' },
//     { eventName: '做了12下深蹲', color: 'orange' ,date:'2021-08-21' },
//     { eventName: '做了30下挺舉',  color: 'blue' ,date:'2021-08-21'},
//     { eventName: '做了35下臥舉', color: 'green',date:'2021-08-21' },
//     { eventName: '做了12下深蹲', color: 'orange' ,date:'2021-09-01' },
//     { eventName: '做了30下挺舉',  color: 'blue' ,date:'2021-09-01'},
//     { eventName: '做了35下臥舉', color: 'green',date:'2021-09-01' },
//     { eventName: '做了12下深蹲', color: 'orange' ,date:'2021-09-05' },
//     { eventName: '做了30下挺舉',  color: 'blue' ,date:'2021-09-05'},
//     { eventName: '做了35下臥舉', color: 'green',date:'2021-09-05' },
//     { eventName: '做了12下深蹲', color: 'orange' ,date:'2021-09-03' },
//     { eventName: '做了30下挺舉',  color: 'blue' ,date:'2021-09-03'},
//     { eventName: '做了35下臥舉', color: 'green',date:'2021-09-03' },    

//     /*
//    { eventName: '做了n下深蹲', calendar: 'Squat', color: 'orange' },
//     { eventName: '做了n下深蹲', calendar: 'Squat', color: 'orange' },
//     { eventName: '做了n下深蹲', calendar: 'Squat', color: 'orange' },
//     { eventName: '做了n下深蹲', calendar: 'Squat', color: 'orange' },

//     { eventName: '做了n下挺舉', calendar: 'Deadlifts', color: 'blue' },
//     { eventName: '做了n下挺舉', calendar: 'Deadlifts', color: 'blue' },
//     { eventName: '做了n下挺舉', calendar: 'Deadlifts', color: 'blue' },
//     { eventName: '做了n下挺舉', calendar: 'Deadlifts', color: 'blue' },


//     { eventName: '做了n下臥舉', calendar: 'clean and jerk', color: 'green' },
//     { eventName: '做了n下臥舉', calendar: 'clean and jerk', color: 'green' },
//     { eventName: '做了n下臥舉', calendar: 'clean and jerk', color: 'green' },
//     { eventName: '做了n下臥舉', calendar: 'clean and jerk', color: 'green' }
//     */
//   ];

  

//   function addDate(ev) {
    
//   }

//   var calendar = new Calendar('#calendar', data);

// }();

// Alert box design by Igor Ferrão de Souza: https://www.linkedin.com/in/igor-ferr%C3%A3o-de-souza-4122407b/

function cuteAlert({
  view,
  type,
  title,
  message,
  buttonText = "OK",
  confirmText = "OK",
  cancelText = "Cancel",
  closeStyle,
  date,
}) {
  return new Promise((resolve) => {
    setInterval(() => {}, 5000);
    const body = document.querySelector("body");

    const scripts = document.getElementsByTagName("script");
    let currScript = "";

    for (let script of scripts) {
      if (script.src.includes("cute-alert.js")) {
        currScript = script;
      }
    }

    let src = currScript.src;

    src = src.substring(0, src.lastIndexOf("/"));

    let closeStyleTemplate = "alert-close";
    if (closeStyle === "circle") {
      closeStyleTemplate = "alert-close-circle";
    }

    let btnTemplate = `
    <button class="alert-button ${type}-bg ${type}-btn">${buttonText}</button>
    `;
    if (type === "question") {
      btnTemplate = `
      <div class="question-buttons">
      <button class="cancel-button error-bg error-btn">${cancelText}</button>
      <button class="confirm-button ${type}-bg ${type}-btn">${confirmText}</button>
      </div>
      `;
    }

    const template = `
    <div class="alert-wrapper">
      <div class="alert-frame">
        <div class="alert-header ${type}-bg">
          <span class="${closeStyleTemplate}">X</span>
        </div>
        <div class="alert-body">
          
          <span class="alert-message">${date}</span>
          <video class="alert-video" muted controls>		
            <source src="../watchout/img/${date}.mp4" type="video/mp4" alt="${date}">  		
            //路徑放在這裡
            </video>

        </div>
        ${btnTemplate}
      </div>
    </div>
    `; 

    body.insertAdjacentHTML("afterend", template);

    const alertWrapper = document.querySelector(".alert-wrapper");
    const alertFrame = document.querySelector(".alert-frame");
    const alertClose = document.querySelector(`.${closeStyleTemplate}`);

    if (type === "question") {
      const confirmButton = document.querySelector(".confirm-button");
      const cancelButton = document.querySelector(".cancel-button");

      confirmButton.addEventListener("click", () => {
        alertWrapper.remove();
        resolve("confirm");
      });

      cancelButton.addEventListener("click", () => {
        alertWrapper.remove();
        resolve();
      });
    } else {
      const alertButton = document.querySelector(".alert-button");

      alertButton.addEventListener("click", () => {
        alertWrapper.remove();
        resolve();
      });
    }

    alertClose.addEventListener("click", () => {
      alertWrapper.remove();
      resolve();
    });

    alertWrapper.addEventListener("click", () => {
      alertWrapper.remove();
      resolve();
    });

    alertFrame.addEventListener("click", (e) => {
      e.stopPropagation();
    });
  });
}