package _2022_Gruppe1130.Lösung;

import java.util.Iterator;

// An iterator over elements of 'Gruppe1130.Gruppe1300.Ingredient'.
//
public interface IngredientIterator extends Iterator<Ingredient> {

    @Override
    // Returns the next element in the iteration.
    Ingredient next();

    @Override
    // Returns 'true' if the iteration has more elements.
    boolean hasNext();
}
