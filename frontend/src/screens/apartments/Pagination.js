import React from "react";

const Paginate = ({ totalPosts, paginate, currentPage }) => {
  const pageNumbers = [];

  for (let i = 1; i <= Math.ceil(totalPosts / 10); i++) {
    pageNumbers.push(i);
  }

  return (
    <div className="pagination-container">
      <ul className="pagination">
        {pageNumbers.map((number) => (
          <li
            key={number}
            onClick={() => paginate(number)}
            className={`page-number ${currentPage === number ? "active" : ""}`}
          >
            {number}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Paginate;
