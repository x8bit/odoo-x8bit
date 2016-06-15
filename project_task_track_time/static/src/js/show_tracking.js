/******************************************************************************
    Web Easy Switch Company module for OpenERP
    Copyright (C) 2014-2015 GRAP (http://www.grap.coop)
    @author Sylvain LE GAL (https://twitter.com/legalsylvain)
    @contributor Nicolas JEUDY (https://github.com/njeudy)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
******************************************************************************/

odoo.define('web.project_task_track_time',function (require) {

    "use strict";

    var NO_TRACKING_MSG = "Not tracking";
    var interval_id  = null;
    var curr_tracking = null;

    var Widget = require('web.Widget');
    var SystrayMenu = require('web.SystrayMenu');
    var web_client = require('web.web_client');
    var Model = require('web.Model');

    /***************************************************************************
    Create an new 'ShowTracking' widget that allow users to switch
    from a company to another more easily.
    ***************************************************************************/
    var ShowTrackingWidget = Widget.extend({

        template:'project_task_track_time.ShowTracking',

        /***********************************************************************
        Overload section
        ***********************************************************************/

        /**
         * Overload 'init' function to initialize the values of the widget.
         */
        init: function(parent){
            this._super(parent);
            // this.date = NO_TRACKING_MSG;
            this._not_tracking();
        },

        /**
         * Overload 'start' function to load datas from DB.
         */
        start: function () {
            var self = this;
            this._super();
            var loop = setInterval(function(){
                self._get_tracking_time();
            }, 1000 * 30);
            self._get_tracking_time();
        },

        /**
         * Overload 'renderElement' function to set events on company items.
         */
        renderElement: function() {
            var self = this;
            this._super();
            this.$el.find('.project_task_track_time_stop_tracking').on('click', function(ev) {
                new Model("project.task").call("stopTrackingTime", [{ uid: self.session.uid }]).then(function(result) {
                    self._not_tracking();
                });
            });
        },

        _not_tracking: function() {
            clearInterval(interval_id);
            this.date = NO_TRACKING_MSG;
            $('.tracking_timer_count', this.$el).html(this.date);
            $('.caret', this.$el).hide();
            $('.dropdown-toggle', this.$el).prop("disabled", true);
        },

        _tracking: function(task, tracking_time) {
            self = this;
            
            clearInterval(interval_id);

            interval_id = setInterval(function(){ 
                self.date = self._calculate_min_secs(tracking_time[0].create_date);
                $('.tracking_timer_count', this.$el).html(self.date);
            }, 1000);

            self.project = task[0].project_id[1];
            self.task = task[0].name;
            self.description = tracking_time[0].description;

            $('.caret', this.$el).show();
            $('.dropdown-toggle', this.$el).prop("disabled", false);

            self.renderElement();
        },


        /***********************************************************************
        Custom section
        ***********************************************************************/

        /**
         * helper function to load data from the server
         */
        _fetch: function(model, fields, domain, ctx){
            return new Model(model).query(fields).filter(domain).context(ctx).all();
        },

        _calculate_min_secs: function(create_date) {
            var sDate = new Date(create_date);

            var d1 = new Date(Date.UTC(
                sDate.getFullYear(),
                sDate.getMonth(),
                sDate.getDate(),
                sDate.getHours(),
                sDate.getMinutes(),
                sDate.getSeconds()
            ));

            var d2 = new Date();

            var hours = Math.floor((d2 - d1) / 1000 / 60 / 60);
            var minutes = Math.floor((d2 - d1) / 1000 / 60  - hours * 60);
            var seconds = Math.floor(((d2 - d1) / 1000) - (hours * 60 * 60) - (minutes * 60))

            if (hours < 10) {hours = "0"+hours;}
            if (minutes < 10 && hours) {minutes = "0"+minutes;}
            if (seconds < 10 && minutes) {seconds = "0"+seconds;}

            if(hours != "00"){
                return hours + ":" + minutes + ":" + seconds;    
            } else if (minutes != "00") {
                return minutes + ":" + seconds;
            } else {
                return seconds;
            }
            
        },

        _get_tracking_time: function(){
            var self = this;
            this._fetch('project.task.tracking',[],[['create_uid','=',this.session.uid]]).then(function(tracking_time){
                if(tracking_time.length > 0) {
                    if(curr_tracking != tracking_time[0].id) {
                        curr_tracking = tracking_time[0].id;
                        self._fetch('project.task',[],[['id','=',tracking_time[0].task_id[0]]]).then(function(task){
                            self._tracking(task, tracking_time);
                        });
                    }
                } else {
                    self._not_tracking();
                }
            });
        },
    });

SystrayMenu.Items.push(ShowTrackingWidget);

});
