import { useEffect, useState } from "react";

const Intro = () => {
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const onPageLoad = () => {
      setIsLoading(false);
    };

    // Check if the page has already loaded
    if (document.readyState === "complete") {
      onPageLoad();
    } else {
      window.addEventListener("load", onPageLoad);
      // Remove the event listener when component unmounts
      return () => window.removeEventListener("load", onPageLoad);
    }
  }, []);

  return (
    <div>
      {!isLoading ? (
        <div className="mainHomePagePhoto">
          <img src="/homepage/homepage.png" alt="Home Page" />
          <div className="coverText">
            <h1>HomieUA</h1>
            <h3>Fuck realtors</h3>
          </div>
        </div>
      ) : (
        <div>Loading...</div>
      )}
    </div>
  );
};

export default Intro;
