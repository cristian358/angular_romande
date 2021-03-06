import { ReloadService } from './../../_services/reload.sevice';
import { PfcService } from '../../_services';
import { Component, OnInit} from '@angular/core';
import { Pfc } from '../../_models';
import { FormGroup, FormControl, Validators} from '@angular/forms';
import 'rxjs/add/operator/switchMap';
import { ToastrService } from 'ngx-toastr';
import { INgxMyDpOptions, IMyDateModel} from 'ngx-mydatepicker';


@Component({
  selector: 'app-pfc-upload',
  templateUrl: './pfc-upload.component.html',
  styleUrls: [
    // '../../../assets/css/styles/nexus.css',
    // '../../../assets/css/styles/layout.css',
    //  '../../../assets/css/styles/theme.css'
   ]
})
export class PfcUploadComponent implements OnInit {
  yeaar: number;
  pfc_market: boolean;
  myFile: File[];
  fileValid = false;
  uploadForm: FormGroup;
  date: FormControl;
  loading = false;
  currentDate = {};
  pfcs: Pfc[] = [];
  disabData = [];
  dateS: String;

  myOptions: INgxMyDpOptions = {
    dateFormat: 'dd.mm.yyyy',
    disableWeekends: true,
    disableDates: this.disabData,
  };

  constructor(private pfcUpload: PfcService,
              private toastr: ToastrService,
              private reloadService:  ReloadService
            ) { }

  ngOnInit() {
    const date =  new Date();
    this.currentDate = { date: { year: date.getFullYear(), month: date.getUTCMonth() + 1, day:  date.getUTCDate() } };
    this.createFormControles();
    this.createForm();
    this.getPfcs();

  }

  getPfcs() {
    this.pfcUpload.getAll().subscribe((data) => {
      this.pfcs = data;
      data.forEach(element => {
        if (element.pfc_id.length === 10) {
          this.disabData.push({
            'day': Number(element['pfc_id'].slice(0, 2)),
            'month': Number(element['pfc_id'].slice(3, 5)),
            'year': Number(element['pfc_id'].slice(6, 10))
          });
        } else {
          this.disabData.push({
            'day': Number(element['pfc_id'].slice(0, 1)),
            'month': Number(element['pfc_id'].slice(2, 4)),
            'year': Number(element['pfc_id'].slice(5, 9))
          });
      }
      });
    }, );
  }


  fileEvent(files: File[]) {
    this.myFile = files;
    if (this.myFile == null) {
      this.fileValid = false;
    } else {
      this.fileValid = true;
    }
  }

  setType(ptype: boolean) {
    this.pfc_market = ptype;
  }

  showSuccess(mesaj: string) { this.toastr.success( mesaj); }
  showError(mesaj: string) { this.toastr.error(mesaj); }

  onSubmit(data: any) {
    this.loading = true;
    const formDataPfc: any = new FormData();
    formDataPfc.append('pfc_market', 'false');

    if (this.myFile) {
      for (let i = 0; i < this.myFile.length; i++) {
        formDataPfc.append('files', this.myFile[i], this.myFile[i].name);
        }
    } else { formDataPfc.append('files', ''); }

    if (String(data['date']['date']['month']).length === 1) {
      const months = '0' + String(data['date']['date']['month']);
      formDataPfc.append('date', String(data['date']['date']['day']) + '.' + months + '.' + String(data['date']['date']['year']));
    } else {
      const months = String(data['date']['date']['month']);
      formDataPfc.append('date', String(data['date']['date']['day']) + '.' + months + '.' + String(data['date']['date']['year']));
    }
    this.pfcUpload.upload(formDataPfc)
    .then(
      res => console.log()
    )
    .catch(
      er => { this.loading = false; }
    )
    .then(
      () => { this.getPfcs();
              this.uploadForm.get('date').reset();
              this.showSuccess('Le fichier a ??t?? t??l??charg??.');
              this.loading = false;
              $('#cancel-btn').click();
              $('body').click();
              // this.router.navigate(['/pfc']);
              this.reloadService.changePfc(true);
            }
    );
  }

  createFormControles() { this.date = new FormControl('', Validators.required); }
  createForm() { this.uploadForm = new FormGroup({ date: this.date }); }
  onDateChanged(event: IMyDateModel): void { this.currentDate = event; }

}
