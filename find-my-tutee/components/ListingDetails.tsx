export class ListingDetails {
  subject: string;
  agency: string;
  pt: string;
  ft: string;
  moe: string;
  url: string;
  description: string;

  constructor(
    subject: string,
    agency: string,
    pt: string,
    ft: string,
    moe: string,
    url: string,
    description: string = "Please visit their website for more details.",
  ) {
    this.subject = subject;
    this.agency = agency;
    this.pt = pt;
    this.ft = ft;
    this.moe = moe;
    this.url = url;
    this.description = description;
  }
}
