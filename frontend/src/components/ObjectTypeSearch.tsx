import { useEffect, useId, useMemo, useRef, useState } from "react";
import type { SchemaNode } from "../types/schema";

interface ObjectTypeSearchProps {
  nodes: SchemaNode[];
  value: string;
  onChange: (value: string) => void;
  onSelect: (id: string) => void;
}

export function ObjectTypeSearch({
  nodes,
  value,
  onChange,
  onSelect,
}: ObjectTypeSearchProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const listId = useId();

  const [open, setOpen] = useState(false);
  const [activeIndex, setActiveIndex] = useState(0);

  const suggestions = useMemo(() => {
    const query = value.trim().toLowerCase();

    if (!query) return [];

    return nodes
      .filter(
        (node) =>
          node.name.toLowerCase().includes(query) ||
          node.id.toLowerCase().includes(query),
      )
      .sort((a, b) => {
        const aStarts = a.name.toLowerCase().startsWith(query);
        const bStarts = b.name.toLowerCase().startsWith(query);

        return Number(bStarts) - Number(aStarts);
      })
      .slice(0, 8);
  }, [nodes, value]);

  useEffect(() => {
    function handleClickOutside(event: PointerEvent) {
      if (
        containerRef.current &&
        !containerRef.current.contains(event.target as Node)
      ) {
        setOpen(false);
      }
    }

    document.addEventListener("pointerdown", handleClickOutside);

    return () => {
      document.removeEventListener("pointerdown", handleClickOutside);
    };
  }, []);

  function selectNode(id: string) {
    onSelect(id);
    setOpen(false);
    setActiveIndex(0);
  }

  return (
    <div className="object-type-search" ref={containerRef}>
      <input
        type="search"
        role="combobox"
        aria-label="Search object types"
        aria-autocomplete="list"
        aria-expanded={open && suggestions.length > 0}
        aria-controls={listId}
        aria-activedescendant={
          open && suggestions.length > 0
            ? `${listId}-${activeIndex}`
            : undefined
        }
        placeholder="Search object types..."
        value={value}
        onFocus={() => setOpen(true)}
        onChange={(event) => {
          onChange(event.target.value);
          setActiveIndex(0);
          setOpen(true);
        }}
        onKeyDown={(event) => {
          if (event.key === "Escape") {
            setOpen(false);
            return;
          }

          if (event.key === "ArrowDown" && suggestions.length > 0) {
            event.preventDefault();
            setOpen(true);
            setActiveIndex((index) =>
              Math.min(index + 1, suggestions.length - 1),
            );
          }

          if (event.key === "ArrowUp" && suggestions.length > 0) {
            event.preventDefault();
            setOpen(true);
            setActiveIndex((index) => Math.max(index - 1, 0));
          }

          if (event.key === "Enter" && suggestions.length > 0) {
            event.preventDefault();
            selectNode(suggestions[activeIndex]?.id ?? suggestions[0].id);
          }
        }}
      />

      {open && suggestions.length > 0 && (
        <div
          id={listId}
          className="object-type-suggestions"
          role="listbox"
        >
          {suggestions.map((node, index) => (
            <div
              key={node.id}
              id={`${listId}-${index}`}
              role="option"
              aria-selected={index === activeIndex}
              className={`object-type-suggestion ${
                index === activeIndex ? "active" : ""
              }`}
              onMouseDown={(event) => event.preventDefault()}
              onClick={() => selectNode(node.id)}
            >
              <strong>{node.name}</strong>
              <small>{node.id}</small>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
