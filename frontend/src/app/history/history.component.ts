import { Component, OnInit } from '@angular/core';
import {HistoryService} from "./../history.service"

@Component({
  selector: 'app-history',
  templateUrl: './history.component.html',
  styleUrls: ['./history.component.css']
})
export class HistoryComponent implements OnInit {
  session: string = null;
  constructor(public service: HistoryService) { }
  array = []
  ngOnInit() {
      this.session = localStorage.getItem('session');
      this.service.get_history(this.session).subscribe((data)=> {
      this.array = data['transaction'];
      });
  }



}
