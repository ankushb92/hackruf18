import { Component, OnInit } from '@angular/core';
import {HistoryService} from "./../history.service"

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  session: string = null;
  constructor(public service: HistoryService) { }
  array = []
  ngOnInit() {
      this.session = localStorage.getItem('session');
      this.service.get_holdings(this.session).subscribe((data)=> {
      this.array = data['holding'];
      console.log(data);
      });
  }



}
