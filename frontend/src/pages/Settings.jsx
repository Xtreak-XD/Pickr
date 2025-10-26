import React, { useState, useEffect, useMemo } from "react";

function computeAge(dobStr) {
  if (!dobStr) return null;
  const dob = new Date(dobStr + "T00:00:00"); // avoid TZ issues
  if (isNaN(dob.getTime())) return null;

  const today = new Date();
  let age = today.getFullYear() - dob.getFullYear();
  const m = today.getMonth() - dob.getMonth();
  if (m < 0 || (m === 0 && today.getDate() < dob.getDate())) age -= 1;
  return age;
}

export const Settings = () => {
  const [darkMode, setDarkMode] = useState(false);
  const [notifications, setNotifications] = useState(true);
  const [birthday, setBirthday] = useState(""); // yyyy-mm-dd
  const age = useMemo(() => computeAge(birthday), [birthday]);

  const [bdayError, setBdayError] = useState("");

  useEffect(() => {
    const saved = JSON.parse(localStorage.getItem("app.settings") || "{}");
    if (typeof saved.darkMode === "boolean") setDarkMode(saved.darkMode);
    if (typeof saved.notifications === "boolean") setNotifications(saved.notifications);
    if (typeof saved.birthday === "string") setBirthday(saved.birthday);
  }, []);

  const validateBirthday = (value) => {
    if (!value) return ""; // optional
    const a = computeAge(value);
    if (a == null) return "Invalid date";
    if (a < 0 || a > 150) return "Age must be between 0 and 150";
    return "";
  };

  const onBirthdayChange = (e) => {
    const v = e.target.value; // yyyy-mm-dd
    setBirthday(v);
    setBdayError(validateBirthday(v));
  };

  const save = () => {
    const err = validateBirthday(birthday);
    setBdayError(err);
    if (err) return;
    localStorage.setItem(
      "app.settings",
      JSON.stringify({
        darkMode,
        notifications,
        birthday: birthday || null,
      })
    );
  };

  const reset = () => {
    setDarkMode(false);
    setNotifications(true);
    setBirthday("");
    setBdayError("");
  };

  return (
    <div className="w-full px-4 sm:px-6 lg:px-8 pt-6 pb-24">
      <h1 className="text-2xl font-bold mb-6">Settings</h1>

      <div className="bg-white/90 rounded-xl border border-gray-200 shadow-sm p-5 space-y-5">
        {/* Dark mode */}
        <div className="flex items-center justify-between">
          <div>
            <p className="font-medium">Dark mode</p>
            <p className="text-sm text-gray-500">Use a dark color theme</p>
          </div>
          <input
            type="checkbox"
            className="h-5 w-5"
            checked={darkMode}
            onChange={(e) => setDarkMode(e.target.checked)}
          />
        </div>

        <hr />

        {/* Notifications */}
        <div className="flex items-center justify-between">
          <div>
            <p className="font-medium">Notifications</p>
            <p className="text-sm text-gray-500">Enable app alerts</p>
          </div>
          <input
            type="checkbox"
            className="h-5 w-5"
            checked={notifications}
            onChange={(e) => setNotifications(e.target.checked)}
          />
        </div>

        <hr />

        {/* Birthday + Age */}
        <div>
          <div className="flex items-end justify-between gap-3">
            <div className="flex-1">
              <p className="font-medium mb-1">Birthday</p>
              <input
                type="date"
                value={birthday}
                onChange={onBirthdayChange}
                className={`block w-full rounded-lg border px-3 py-2 text-sm focus:outline-none focus:ring-2 ${
                  bdayError
                    ? "border-red-400 focus:ring-red-400"
                    : "border-gray-300 focus:ring-black"
                }`}
              />
              {bdayError && (
                <p className="mt-1 text-sm text-red-600">{bdayError}</p>
              )}
              <p className="mt-1 text-xs text-gray-500">
                Optional. We only store the date locally on this device.
              </p>
            </div>

            {/* Live Age display */}
            <div className="min-w-[7rem] text-right">
              <p className="text-sm text-gray-500">Age</p>
              <p className="text-base font-semibold">
                {birthday && age != null ? `${age} yrs` : "—"}
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Actions */}
      <div className="mt-4 flex gap-3">
        <button
          onClick={reset}
          className="rounded-lg bg-black border-gray-300 text-white px-4 py-2 text-sm font-medium hover:bg-gray-900 cursor-pointer"
        >
          Reset
        </button>
        <button
          onClick={save}
          className="rounded-lg bg-black text-white px-4 py-2 text-sm font-medium hover:bg-gray-900 cursor-pointer"
        >
          Save changes
        </button>
        <a
          href="/login"
          className="ml-auto rounded-lg border border-red-300 text-red-600 px-4 py-2 text-sm font-medium hover:bg-red-50 cursor-pointer"
        >
          Sign out
        </a>
      </div>
    </div>
  );
};
