import { months, days } from "./constants";

export const timeConvert = (timestamp) => {
  let a = new Date(timestamp * 1000);
  const year = a.getFullYear();
  const month = months[a.getMonth()];
  const date = a.getDate();
  return { year, month, date };
};
