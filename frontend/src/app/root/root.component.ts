import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './root.component.html',
  styleUrls: ['./root.component.css']
})
export class RootComponent implements OnInit {

  @Input() userSession: string;
  @Input() user: object;
  constructor() { }

  ngOnInit() {
  }

}
