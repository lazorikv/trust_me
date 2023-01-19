import { months, days } from "./constants";
import { useEffect } from "react";
import { useLocation } from "react-router-dom";
export const timeConvert = (timestamp) => {
  let a = new Date(timestamp * 1000);
  const year = a.getFullYear();
  const month = months[a.getMonth()];
  const date = a.getDate();
  return (
    <span>
      {date} {month} {year}
    </span>
  );
};

export function ScrollToTop() {
  const { pathname } = useLocation();

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [pathname]);

  return null;
}

export function declOfNum(n, text_forms) {
  n = Math.abs(n) % 100;
  let n1 = n % 10;
  if (n > 10 && n < 20) {
    return text_forms[2];
  }
  if (n1 > 1 && n1 < 5) {
    return text_forms[1];
  }
  if (n1 === 1) {
    return text_forms[0];
  }
  return text_forms[2];
}
